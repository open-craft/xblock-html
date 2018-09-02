"""This XBlock will help creating a secure and easy-to-use HTML blocks in edx-platform."""

import logging
import pkg_resources
from xblock.core import XBlock
from xblock.fields import Scope, String

from xblock.fragment import Fragment

from .bleaching import SanitizedText
from .utils import _

log = logging.getLogger('XBlock.HTML')  # pylint: disable=invalid-name


class HTML5XBlock(XBlock):
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
        frag.initialize_js('HTMLXBlock')
        return frag

    def studio_view(self, context=None):  # pylint: disable=unused-argument
        html = self.resource_string('static/html/studio.html')
        frag = Fragment(html.format(self=self))
        self.add_scripts(frag)

        frag.initialize_js('HTML5XBlock')
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

    def add_scripts(self, frag):
        """
        A helper method to add all necessary scripts to the fragment.
        :param frag: The fragment that will hold the scripts.
        """
        frag.add_javascript(self.resource_string('static/js/tinymce/tinymce.min.js'))
        frag.add_javascript(self.resource_string('static/js/tinymce/themes/modern/theme.min.js'))
        frag.add_javascript(self.resource_string('static/js/entrypoint.js'))

    @property
    def sanitized_data(self):
        return SanitizedText(self.data)
