"""
HTML XBlock tests
"""
from __future__ import print_function

import unittest

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
        field_data = DictFieldData({'data': 'Safe <b>html</b>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.allow_javascript, False)
        fragment = block.student_view()
        self.assertIn('<div>Safe <b>html</b></div>', fragment.content)

    def test_render_with_unsafe(self):
        field_data = DictFieldData({'data': 'Safe <b>html</b><script>alert(\'javascript\');</script>'})
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.allow_javascript, False)
        fragment = block.student_view()
        self.assertIn(
            '<div>Safe <b>html</b>&lt;script&gt;alert(\'javascript\');&lt;/script&gt;</div>',
            fragment.content
        )

    def test_render_allow_js(self):
        field_data = DictFieldData({
            'data': 'Safe <b>html</b><script>alert(\'javascript\');</script>',
            'allow_javascript': True
        })
        block = html_xblock.HTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.allow_javascript, True)
        fragment = block.student_view()
        self.assertIn('<div>Safe <b>html</b><script>alert(\'javascript\');</script></div>', fragment.content)
