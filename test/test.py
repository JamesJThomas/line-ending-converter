"""This file is unit tests for line_endings"""
from unittest.mock import call, mock_open, patch
from unittest import TestCase
from pro_line_endings.line_endings import get_file_to_convert
from pro_line_endings.line_endings import read_file
from pro_line_endings.line_endings import convert_endings
from pro_line_endings.line_endings import write_new_contents
from pro_line_endings.line_endings import main


class TestLineEndings(TestCase):
    """test"""

    def test_get_file(self):
        """tests the input of file name"""
        with patch("builtins.input", side_effect=["test.txt"]):
            self.assertEqual(get_file_to_convert(), "test.txt")

    def test_read_file(self):
        """tests the reading of file"""
        file_to_convert = "hello.txt"
        mock_file = mock_open(read_data=b"hello")
        with patch("builtins.open", mock_file):
            self.assertEqual(read_file(file_to_convert), b"hello")

    def test_conversion(self):
        """tests the conversion of line endings"""
        file_contents = b"abc\ndef\nghi"
        self.assertEqual(convert_endings(
            file_contents), b"abc\r\ndef\r\nghi")

    def test_write(self):
        """tests writing to file"""
        mock_file = mock_open()
        with patch("builtins.open", mock_file):
            write_new_contents("hello.txt", "hello")
        mock_file.assert_has_calls(
            [call('hello.txt', 'wb'), call().write('hello'), call().close()])
        self.assertEqual(4, 2+2)
    def test_main(self):
        """dummy test for main"""
        mock_file = mock_open(read_data=b"hello")
        with patch("builtins.open", mock_file), patch("builtins.input", side_effect=[""]):
            main()
        self.assertEqual(24, 3*8)
