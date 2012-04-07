from django.db import models

from markupmirror.fields import MarkupMirrorField


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = MarkupMirrorField('post body')
    comment = MarkupMirrorField(
        escape_html=True, default_markup_type='markdown')

    def __unicode__(self):
        return self.title


class Article(models.Model):
    normal_field = MarkupMirrorField()
    default_field = MarkupMirrorField(default_markup_type='markdown')
    markdown_field = MarkupMirrorField(markup_type='markdown')


class Abstract(models.Model):
    content = MarkupMirrorField()

    class Meta:
        abstract = True


class Concrete(Abstract):
    pass
