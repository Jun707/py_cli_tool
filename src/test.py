import unittest
import webbrowser
import os
from unittest.mock import mock_open, call, patch
from cli import read_files_url, save_input_url, remove_url_input


class Test(unittest.TestCase):

    @patch('cli.webbrowser.open')
    @patch('cli.open', new_callable = mock_open, read_data = "www.google.com\nwww.github.com\n")
    def test_read_url(self, mock_file, mock_webbrowser_open):

        with patch('builtins.print') as mocked_print:
            read_files_url(None)

        expected_calls = [call('www.google.com'), call('www.github.com')]
        mock_webbrowser_open.assert_has_calls(expected_calls, any_order = False)

        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "url_storage.txt")

        mock_file.assert_called_once_with(file_path, 'r')
        mocked_print.assert_called_once_with(['www.google.com', 'www.github.com'])
        
    
    @patch('cli.open', new_callable = mock_open)
    def test_save_input_url(self, mock_file):
        args = type('Args', (object,), {'operands': 'www.yahoo.com'})()

        with patch('builtins.print') as mocked_print:
            save_input_url(args)

        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "url_storage.txt")

        mock_file.assert_any_call(file_path, 'r')
        mock_file.assert_any_call(file_path, 'a')

        mock_file().write.assert_called_once_with('www.yahoo.com\n')
        mocked_print.assert_called_once_with('www.yahoo.com is saved')

    @patch('cli.open', new_callable = mock_open, read_data = "www.yahoo.com\nwww.google.com\n")
    def test_save_input_url_with_duplicated_url(self, mock_file):
        args = type('Args', (object,), {'operands': 'www.yahoo.com'})()

        with patch('builtins.print') as mocked_print:
            save_input_url(args)

        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "url_storage.txt")

        mock_file.assert_called_once_with(file_path, 'r')

        mocked_print.assert_called_once_with('www.yahoo.com has exits')
    
    @patch('cli.open', new_callable = mock_open,
            read_data = "www.google.com\nwww.github.com\nwww.yahoo.com\n")
    def test_remove_url_input(args, mock_file):
        args = type('Args', (object,), {'operands': 'www.yahoo.com'})()

        with patch('builtins.print') as mocked_print:
            remove_url_input(args)
        
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "url_storage.txt")

        mock_file.assert_any_call(file_path, 'r')
        mock_file.assert_any_call(file_path, 'w')
        mock_file().writelines.assert_has_calls([call('www.google.com\n'), call('www.github.com\n')])
        mocked_print.assert_called_once_with('www.yahoo.com is removed')



if __name__ == "__main__":
    unittest.main()