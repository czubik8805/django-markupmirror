from django.test import TestCase

from markupmirror.feincms.models import MarkupMirrorContent


class FeinCMSTests(TestCase):
    """Tests the ``markupmirror.feincms`` module that provides integration
    into FeinCMS as page content-type.

    """
    def test_import(self):
        """The ``markupmirror.feincms`` app can only be installed when
        FeinCMS is installed.

        """
        # returns True if feincms is installed or False otherwise
        def import_markupmirror_feincms():
            try:
                import markupmirror.feincms
                return True
            except ImportError:
                return False

        # unregister previous imports
        import sys
        to_delete = [module for module in sys.modules
            if (module.startswith('markupmirror.feincms') or
                module.startswith('feincms'))]
        for module in to_delete:
            del sys.modules[module]
        self.assertFalse('markupmirror.feincms' in sys.modules)
        self.assertFalse('feincms' in sys.modules)

        # save original import
        import __builtin__
        original_import = __builtin__.__import__

        # patch and test the import
        def import_hook(name, *args, **kwargs):
            if name in 'feincms':
                raise ImportError("TestCase ImportError")
            else:
                original_import(name, *args, **kwargs)
        __builtin__.__import__ = import_hook

        # without FeinCMS, the import should fail
        self.assertFalse(import_markupmirror_feincms())

        # with FeinCMS installed, the import should work
        # restore import
        __builtin__.__import__ = original_import
        self.assertTrue(import_markupmirror_feincms())

        # restore normal import
        from markupmirror.feincms import models
        self.assertTrue('markupmirror.feincms' in sys.modules)
        self.assertTrue('markupmirror.feincms.models' in sys.modules)

    def test_markupmirror_content(self):
        """
        """
        from feincms.module.page.models import Page
        from markupmirror.feincms.models import MarkupMirrorContent
        Page.register_templates({
            'key': 'page',
            'title': 'Page template',
            'path': 'feincms_page.html',
            'regions': (
                ('main', 'Main region'),
                ),
        })
        Page.create_content_type(MarkupMirrorContent)
