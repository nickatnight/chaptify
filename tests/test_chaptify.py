from unittest import TestCase

from chaptify.utils import clean_line


class ChaptifyUtilsTestCase(TestCase):
    def test_clean_line_single_digit(self):
        """test line is parsed correctly"""
        data = {"title": "9..FRM - Decay"}
        assert "FRM - Decay" == clean_line(data)

    def test_clean_line_double_digit(self):
        """test line is parsed correctly"""
        data = {"title": "35..Florida Skyline - Blueberry"}
        assert "Florida Skyline - Blueberry" == clean_line(data)
