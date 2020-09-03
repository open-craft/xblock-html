"""
HTML XBlock tests
"""
from __future__ import print_function

import unittest

from mock import Mock
from xblock.field_data import DictFieldData
from xblock.test.tools import TestRuntime

import html_xblock


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
        self.assertIn('<div class="html_block">Safe <b>html</b></div>', fragment.content)

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
            '<div class="html_block">Safe <b>html</b>&lt;script&gt;alert(\'javascript\');&lt;/script&gt;</div>',
            fragment.content
        )

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
        self.assertIn('<div class="html_block">Safe <b>html</b><script>alert(\'javascript\');</script></div>',
                      fragment.content)

    def test_substitution_no_system(self):
        """
        Test that the substitution is not performed when `system` is not present inside XBlock.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%USER_ID%% %%COURSE_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        fragment = block.student_view()
        self.assertIn('<div class="html_block">Safe <b>%%USER_ID%% %%COURSE_ID%%</b></div>', fragment.content)

    def test_substitution_not_found(self):
        """
        Test that the keywords are not replaced when they're not found.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%USER_ID%% %%COURSE_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        block.system = Mock(anonymous_student_id=None)
        fragment = block.student_view()
        self.assertIn('<div class="html_block">Safe <b>%%USER_ID%% %%COURSE_ID%%</b></div>', fragment.content)

    def test_user_id_substitution(self):
        """
        Test replacing %%USER_ID%% with anonymous user ID.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%USER_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        block.system = Mock(anonymous_student_id='test_user')
        fragment = block.student_view()
        self.assertIn('<div class="html_block">Safe <b>test_user</b></div>', fragment.content)

    def test_course_id_substitution(self):
        """
        Test replacing %%COURSE_ID%% with HTML representation of course key.
        """
        field_data = DictFieldData({'data': 'Safe <b>%%COURSE_ID%%</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        course_locator_mock = Mock()
        course_locator_mock.html_id = Mock(return_value='test_course')
        block.system = Mock(course_id=course_locator_mock)
        fragment = block.student_view()
        self.assertIn('<div class="html_block">Safe <b>test_course</b></div>', fragment.content)
