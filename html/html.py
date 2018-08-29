"""This XBlock will help creating and using a secure and easy-to-use HTML blocks."""

import logging
import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String

from xblock.fragment import Fragment

from .utils import _

log = logging.getLogger('XBlock.HTML')


class HTMLXBlock(XBlock):
    """
    TODO: document what your XBlock does.
    """
    display_name = String(
        display_name=_("Display Name"),
        help=_("The display name for this component."),
        scope=Scope.settings,
        # it'd be nice to have a useful default but it screws up other things; so,
        # use display_name_with_default for those
        default=_("Text")
    )
    data = String(help=_("Html contents to display for this module"), default=u"", scope=Scope.content)
    editor = String(
        help=_(
            "Select Visual to enter content and have the editor automatically create the HTML. Select Raw to edit "
            "HTML directly. If you change this setting, you must save the component and then re-open it for editing."
        ),
        display_name=_("Editor"),
        default="visual",
        values=[
            {"display_name": _("Visual"), "value": "visual"},
            {"display_name": _("Raw"), "value": "raw"}
        ],
        scope=Scope.settings
    )

    def resource_string(self, path):  # pylint: disable=no-self-use
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    @XBlock.supports("multi_device")
    def student_view(self, context=None):  # pylint: disable=unused-argument
        """
        The primary view of the HTMLXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/html.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/html.css"))
        frag.add_javascript(self.resource_string("static/js/src/html.js"))
        frag.initialize_js('HTMLXBlock')
        return frag

    # TODO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):  # pylint: disable=unused-argument
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TODO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("HTMLXBlock",
             """<html/>
             """),
            ("Multiple HTMLXBlock",
             """<vertical_demo>
                <html/>
                <html/>
                <html/>
                </vertical_demo>
             """),
        ]
