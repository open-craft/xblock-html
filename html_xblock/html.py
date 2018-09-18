"""This XBlock will help creating a secure and easy-to-use HTML blocks in edx-platform."""

import logging
import pkg_resources
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin, loader as studio_editable_loader

from .bleaching import SanitizedText
from .utils import _

log = logging.getLogger('XBlock.HTML')  # pylint: disable=invalid-name
loader = ResourceLoader(__name__)  # pylint: disable=invalid-name


class HTML5XBlock(StudioEditableXBlockMixin, XBlock):
    """
    This XBlock will provide an HTML WYSIWYG interface in Studio to be rendered in LMS.
    """
    display_name = String(
        display_name=_('Display Name'),
        help=_('The display name for this component.'),
        scope=Scope.settings,
        default=_('Text')
    )
    data = String(help=_('Html contents to display for this module'), default=u'', scope=Scope.content)
    editor = String(
        help=_(
            'Select Visual to enter content and have the editor automatically create the HTML. Select Raw to edit '
            'HTML directly. If you change this setting, you must save the component and then re-open it for editing.'
        ),
        display_name=_('Editor'),
        default='visual',
        values=[
            {'display_name': _('Visual'), 'value': 'visual'},
            {'display_name': _('Raw'), 'value': 'raw'}
        ],
        scope=Scope.settings
    )
    editable_fields = ('display_name', 'editor')

    @staticmethod
    def resource_string(path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode('utf8')

    @XBlock.supports('multi_device')
    def student_view(self, context=None):  # pylint: disable=unused-argument
        """
        Return a fragment that contains the html for the student view
        """
        html = self.resource_string('static/html/lms.html')
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string('public/plugins/codesample/css/prism.css'))
        frag.add_javascript(self.resource_string('public/plugins/codesample/js/prism.js'))

        return frag

    def studio_view(self, context=None):  # pylint: disable=unused-argument
        frag = Fragment()
        context = {
            'self': self,
            'settings_template': studio_editable_loader.render_template('templates/studio_edit.html', {
                'fields': self.get_editable_fields()
            }),
        }
        frag.content = loader.render_template('static/html/studio.html', context)

        self.add_stylesheets(frag)
        self.add_scripts(frag)

        data = {
            'editor': self.editor,
            'skin_url': self.runtime.local_resource_url(self, 'public/skin'),
            'external_plugins': self.get_editor_plugins()
        }
        frag.initialize_js('HTML5XBlock', data)

        return frag

    @XBlock.json_handler
    def update_content(self, data, suffix=''):  # pylint: disable=unused-argument
        """
        This method will update the field, data content with the submitted data from studio_view
        """
        self.data = data['content']

        return {'content': self.data}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ('HTML5XBlock',
             """<html5/>
             """),
            ('Multiple HTML5XBlock',
             """<vertical_demo>
                <html5/>
                <html5/>
                <html5/>
                </vertical_demo>
             """),
        ]

    def add_stylesheets(self, frag):
        """
        A helper method to add all necessary styles to the fragment.
        :param frag: The fragment that will hold the scripts.
        """
        frag.add_css(self.resource_string('static/css/html.css'))

        if self.editor != 'visual':
            frag.add_css(self.resource_string('public/plugins/codemirror/codemirror-4.8/lib/codemirror.css'))

    def add_scripts(self, frag):
        """
        A helper method to add all necessary scripts to the fragment.
        :param frag: The fragment that will hold the scripts.
        """
        frag.add_javascript(self.resource_string('static/js/tinymce/tinymce.min.js'))
        frag.add_javascript(self.resource_string('static/js/tinymce/themes/modern/theme.min.js'))
        frag.add_javascript(self.resource_string('static/js/html.js'))
        frag.add_javascript(studio_editable_loader.load_unicode('public/studio_edit.js'))

        if self.editor != 'visual':
            code_mirror_dir = 'public/plugins/codemirror/codemirror-4.8/'
            frag.add_javascript(self.resource_string(code_mirror_dir + 'lib/codemirror.js'))
            frag.add_javascript(self.resource_string(code_mirror_dir + 'mode/xml/xml.js'))

    def get_editor_plugins(self):
        """
        This method will generate a list of external plugins urls to be used in TinyMCE editor.
        These plugins should live in `public` directory for us to generate URLs for.

        const PLUGINS_DIR = "/resource/html5/public/plugins/";
        const EXTERNAL_PLUGINS = PLUGINS.map(function(p) { return PLUGINS_DIR + p + "/plugin.min.js" });

        :return: A list of URLs
        """
        plugins_dir = 'public/plugins/'
        plugin_file = '/plugin.min.js'
        plugins = ['codesample', 'image', 'link', 'lists', 'textcolor', 'codemirror']

        return {
            plugin: self.runtime.local_resource_url(self, plugins_dir + plugin + plugin_file) for plugin in plugins
        }

    @property
    def sanitized_data(self):
        return SanitizedText(self.data)

    def get_editable_fields(self):
        fields = []
        # Build a list of all the fields that can be edited:
        for field_name in self.editable_fields:
            field = self.fields[field_name]  # pylint: disable=unsubscriptable-object
            assert field.scope in (Scope.content, Scope.settings), (
                'Only Scope.content or Scope.settings fields can be used with '
                'StudioEditableXBlockMixin. Other scopes are for user-specific data and are '
                'not generally created/configured by content authors in Studio.'
            )
            field_info = self._make_field_info(field_name, field)
            if field_info is not None:
                fields.append(field_info)

        return fields
