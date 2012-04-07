from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe

from markupmirror import widgets
from markupmirror.markup.base import markup_pool


# suffixes for rendered and markup_type fields
_rendered_field_name = lambda name: '_%s_rendered' % name
_markup_type_field_name = lambda name: '%s_markup_type' % name

# get available markup types from markup_pool
_MARKUP_TYPES = markup_pool.get_all_markups()


class Markup(object):
    """Wrapper class for markup content output.

    Stores the names of the associated field, the rendered field and the
    markup_type field to make assignment possible.

    """
    def __init__(self, instance, field_name,
                 rendered_field_name, markup_type_field_name):
        self.instance = instance
        self.field_name = field_name
        self.rendered_field_name = rendered_field_name
        self.markup_type_field_name = markup_type_field_name

    @property
    def raw(self):
        return self.instance.__dict__[self.field_name]

    @raw.setter
    def raw(self, value):
        return setattr(self.instance, self.field_name, value)

    @property
    def markup_type(self):
        return self.instance.__dict__[self.markup_type_field_name]

    @markup_type.setter
    def markup_type(self, value):
        return setattr(self.instance, self.markup_type_field_name, value)

    @property
    def rendered(self):
        return getattr(self.instance, self.rendered_field_name)

    def __unicode__(self):
        """Allows display via templates to work without safe filter."""
        return mark_safe(self.rendered)


class MarkupMirrorFieldDescriptor(object):
    """Descriptor class for field functionality."""

    def __init__(self, field):
        self.field = field
        self.rendered_field_name = _rendered_field_name(self.field.name)
        self.markup_type_field_name = _markup_type_field_name(self.field.name)

    def __get__(self, instance, owner):
        if instance is None:
            raise AttributeError("Requires MarkupMirrorField instance")
        markup = instance.__dict__[self.field.name]
        if markup is None:
            return None
        return Markup(instance, self.field.name,
                      self.rendered_field_name, self.markup_type_field_name)

    def __set__(self, obj, value):
        if isinstance(value, Markup):
            obj.__dict__[self.field.name] = value.raw
            setattr(obj, self.rendered_field_name, value.rendered)
            setattr(obj, self.markup_type_field_name, value.markup_type)
        else:
            obj.__dict__[self.field.name] = value


class MarkupMirrorField(models.TextField):
    """Field to store markup content.

    MarkupMirrorField adds three fields to the model it is used in.

    * One field for the raw markup content.
    * One field for the rendered HTML content.
    * One field that specifies the markup type.

    """
    def __init__(self, verbose_name=None, name=None,
                 markup_type=None, default_markup_type=None,
                 markup_choices=_MARKUP_TYPES, escape_html=False,
                 **kwargs):

        if markup_type and default_markup_type:
            raise ImproperlyConfigured(
                "Cannot specify both markup_type and default_markup_type")

        self.default_markup_type = markup_type or default_markup_type
        self.markup_type_editable = markup_type is None
        self.escape_html = escape_html

        # TODO: this was a list of tuples originally
        self.markup_choices_list = sorted(markup_choices.keys())
        self.markup_choices_dict = markup_choices

        if (self.default_markup_type and
            self.default_markup_type not in self.markup_choices_list):
            raise ImproperlyConfigured(
                "Invalid default_markup_type for field '%s', "
                "available types: %s" % (
                    name, ', '.join(self.markup_choices_list)))

        # for South FakeORM compatibility: the frozen version of a
        # MarkupMirrorField can't try to add a _rendered field, because the
        # _rendered field itself is frozen as well. See introspection
        # rules below.
        self.rendered_field = not kwargs.pop('rendered_field', False)

        super(MarkupMirrorField, self).__init__(verbose_name, name, **kwargs)

    def contribute_to_class(self, cls, name):
        """Adds two additional fields for rendered HTML content and markup type
        to the model.

        """
        if not cls._meta.abstract:
            # markup_type
            choices = zip(self.markup_choices_list, self.markup_choices_list)
            markup_type_field = models.CharField(
                choices=choices, max_length=30,
                default=self.default_markup_type, blank=self.blank,
                editable=self.markup_type_editable)
            markup_type_field.creation_counter = self.creation_counter + 1

            # rendered
            rendered_field = models.TextField(editable=False)
            rendered_field.creation_counter = self.creation_counter + 2

            # add fields to class
            cls.add_to_class(_markup_type_field_name(name), markup_type_field)
            cls.add_to_class(_rendered_field_name(name), rendered_field)

        super(MarkupMirrorField, self).contribute_to_class(cls, name)

        # use MarkupMirrorFieldDescriptor to access this field
        setattr(cls, self.name, MarkupMirrorFieldDescriptor(self))

    def pre_save(self, model_instance, add):
        value = super(MarkupMirrorField, self).pre_save(model_instance, add)

        # check for valid markup type
        if value.markup_type not in self.markup_choices_list:
            raise ValueError(
                'Invalid markup type (%s), available types: %s' % (
                    value.markup_type,
                    ', '.join(self.markup_choices_list)))

        # escape HTML
        if self.escape_html:
            raw = escape(value.raw)
        else:
            raw = value.raw

        rendered = self.markup_choices_dict[value.markup_type](raw)
        setattr(model_instance, _rendered_field_name(self.attname), rendered)
        return value.raw

    def get_prep_value(self, value):
        if isinstance(value, Markup):
            return value.raw
        else:
            return value

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return value.raw

    def formfield(self, **kwargs):
        defaults = {'widget': widgets.MarkupMirrorTextarea}
        defaults.update(kwargs)
        return super(MarkupMirrorField, self).formfield(**defaults)


# register MarkupMirrorField to use the custom widget in the Admin
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS

FORMFIELD_FOR_DBFIELD_DEFAULTS[MarkupMirrorField] = {
    'widget': widgets.AdminMarkupMirrorTextareaWidget,
}


# allow South to handle MarkupMirrorField smoothly
try:
    from south.modelsinspector import add_introspection_rules
    # For a normal MarkupMirrorField, the add_rendered_field attribute is
    # always True, which means no_rendered_field arg will always be
    # True in a frozen MarkupMirrorField, which is what we want.
    add_introspection_rules(
        rules=[
            ((MarkupMirrorField,), [], {
                'rendered_field': ['rendered_field', {}],
            })
        ],
        patterns=['markupmirror\.fields\.MarkupMirrorField'])
except ImportError:
    pass
