"""
HTML XBlock tests
"""
from __future__ import print_function

import unittest

from mock import Mock
from xblock.field_data import DictFieldData
from xblock.test.tools import TestRuntime

import html_xblock

TABLE_HTML = """
<table border="1" cellpadding="1" cellspacing="1" style="background-color: #c2e0f4; border-collapse: collapse; border-color: blue; border-style: solid; height: 50px; margin-left: auto; margin-right: auto; width: 100%;"><caption></caption>
<thead>
<tr style="height: 10px; background-color: #2dc26b; border-color: green; border-style: solid; text-align: center;">
<td scope="col" style="width: 33.1779%;"></td>
<td scope="col" style="width: 33.1779%;"></td>
<td scope="col" style="width: 33.1779%;"></td>
</tr>
</thead>
<tbody>
<tr>
<td style="width: 33.1779%;"></td>
<td style="width: 33.1779%; height: 10px; background-color: #3598db; text-align: center; vertical-align: middle; border: 2px solid #236fa1;"></td>
<td style="width: 33.1779%;"></td>
</tr>
</tbody>
<tfoot>
<tr style="height: 10px; background-color: #b96ad9; border-color: purple; border-style: solid; text-align: center;">
<td style="width: 33.1779%;"></td>
<td style="width: 33.1779%;"></td>
<td style="width: 33.1779%;"></td>
</tr>
</tfoot>
</table>
"""  # noqa: E501


class TestHTMLXBlock(unittest.TestCase):
    """
    Unit tests for `html_xblock`
    """
    def setUp(self):
        self.runtime = TestRuntime()

    def test_render(self):
        """
        Test a basic rendering with default settings.
        """
        field_data = DictFieldData({'data': 'Safe <b>html</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.allow_javascript, False)
        fragment = block.student_view()
        self.assertIn('Safe <b>html</b>', fragment.content)

    def test_render_with_unsafe(self):
        """
        Test a basic rendering with default settings.
        Expects the content to be sanitized.
        """
        field_data = DictFieldData({'data': 'Safe <b>html</b><script>alert(\'javascript\');</script>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.allow_javascript, False)
        fragment = block.student_view()
        self.assertIn(
            'Safe <b>html</b>&lt;script&gt;alert(\'javascript\');&lt;/script&gt;',
            fragment.content
        )

    def test_render_table_without_allow_js(self):
        """
        Test that tables are rendered correctly without allowing js.
        """
        field_data = DictFieldData({'data': TABLE_HTML})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.allow_javascript, False)
        fragment = block.student_view()
        self.assertIn(TABLE_HTML, fragment.content)

    def test_render_allow_js(self):
        """
        Test a basic rendering with javascript enabled.
        Expects the content *not* to be sanitized.
        """
        field_data = DictFieldData({
            'data': 'Safe <b>html</b><script>alert(\'javascript\');</script>',
            'allow_javascript': True
        })
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.allow_javascript, True)
        fragment = block.student_view()
        self.assertIn('Safe <b>html</b><script>alert(\'javascript\');</script>', fragment.content)

    def test_substitution_no_runtime(self):
        """
        Test that the substitution is not performed when `runtime` is not present inside XBlock.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%USER_ID%% %%COURSE_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        fragment = block.student_view()
        self.assertIn('Safe <b>%%USER_ID%% %%COURSE_ID%%</b>', fragment.content)

    def test_substitution_not_found(self):
        """
        Test that the keywords are not replaced when they're not found.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%USER_ID%% %%COURSE_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        block.runtime = Mock(anonymous_student_id=None)
        fragment = block.student_view()
        self.assertIn('Safe <b>%%USER_ID%% %%COURSE_ID%%</b>', fragment.content)

    def test_user_id_substitution(self):
        """
        Test replacing %%USER_ID%% with anonymous user ID.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%USER_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        block.runtime = Mock(anonymous_student_id='test_user')
        fragment = block.student_view()
        self.assertIn('Safe <b>test_user</b>', fragment.content)

    def test_course_id_substitution(self):
        """
        Test replacing %%COURSE_ID%% with HTML representation of course key.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%COURSE_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        course_locator_mock = Mock()
        course_locator_mock.html_id = Mock(return_value='test_course')
        block.runtime = Mock(course_id=course_locator_mock)
        fragment = block.student_view()
        self.assertIn('Safe <b>test_course</b>', fragment.content)
