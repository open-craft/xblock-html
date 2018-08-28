"""This XBlock will help creating and using a secure and easy-to-use HTML blocks."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.fragment import Fragment


class HTMLXBlock(XBlock):
    """
    TODO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TODO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):  # pylint: disable=no-self-use
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TODO: change this view to display your data your own way.
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
