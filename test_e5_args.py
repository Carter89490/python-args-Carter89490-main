import pytest
from unittest.mock import patch
from e5_args import main
import re

def test_main_calls_list_files_and_directories():
    with patch('e5_args.list_files_and_directories') as mock_list_files:
        with patch('e5_args.delete_file_or_directory') as mock_delete:
            with patch('e5_args.rename_file_or_directory') as mock_rename:
                with patch('e5_args.search_file_by_name') as mock_search:
                    # Mock the command-line arguments
                    with patch('sys.argv', ['your_script.py', 'path/to/directory', '--list']):
                        main()

    # Check if the list_files_and_directories function was called
    mock_list_files.assert_called_once_with('path/to/directory')

    # Check if the other functions were not called
    mock_delete.assert_not_called()
    mock_rename.assert_not_called()
    mock_search.assert_not_called()

def test_main_calls_delete_file_or_directory():
    with patch('e5_args.list_files_and_directories') as mock_list_files:
        with patch('e5_args.delete_file_or_directory') as mock_delete:
            with patch('e5_args.rename_file_or_directory') as mock_rename:
                with patch('e5_args.search_file_by_name') as mock_search:
                    # Mock the command-line arguments
                    with patch('sys.argv', ['your_script.py', 'path/to/file.txt', '--delete']):
                        main()

    # Check if the delete_file_or_directory function was called
    mock_delete.assert_called_once_with('path/to/file.txt')

    # Check if the other functions were not called
    mock_list_files.assert_not_called()
    mock_rename.assert_not_called()
    mock_search.assert_not_called()

def test_main_calls_rename_file_or_directory():
    with patch('e5_args.list_files_and_directories') as mock_list_files:
        with patch('e5_args.delete_file_or_directory') as mock_delete:
            with patch('e5_args.rename_file_or_directory') as mock_rename:
                with patch('e5_args.search_file_by_name') as mock_search:
                    # Mock the command-line arguments
                    with patch('sys.argv', ['your_script.py', 'old_path', '--rename', 'new_name']):
                        main()

    # Check if the rename_file_or_directory function was called
    mock_rename.assert_called_once_with('old_path', 'new_name')

    # Check if the other functions were not called
    mock_list_files.assert_not_called()
    mock_delete.assert_not_called()
    mock_search.assert_not_called()

def test_main_calls_search_file_by_name():
    with patch('e5_args.list_files_and_directories') as mock_list_files:
        with patch('e5_args.delete_file_or_directory') as mock_delete:
            with patch('e5_args.rename_file_or_directory') as mock_rename:
                with patch('e5_args.search_file_by_name') as mock_search:
                    # Mock the command-line arguments
                    with patch('sys.argv', ['your_script.py', 'path/to/directory', '--search', 'file.txt']):
                        main()

    # Check if the search_file_by_name function was called
    mock_search.assert_called_once_with('path/to/directory', 'file.txt')

    # Check if the other functions were not called
    mock_list_files.assert_not_called()
    mock_delete.assert_not_called()
    mock_rename.assert_not_called()

def test_main_no_args(capsys):
    with patch('e5_args.list_files_and_directories') as mock_list_files:
        with patch('e5_args.delete_file_or_directory') as mock_delete:
            with patch('e5_args.rename_file_or_directory') as mock_rename:
                with patch('e5_args.search_file_by_name') as mock_search:
                    # Mock the command-line arguments
                    with patch('sys.argv', ['your_script.py']):
                        with pytest.raises(SystemExit) as exc_info:
                            main()

    # Check if no functions were called
    mock_list_files.assert_not_called()
    mock_delete.assert_not_called()
    mock_rename.assert_not_called()
    mock_search.assert_not_called()

    assert exc_info.value.code == 2

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert "the following arguments are required: directory" in captured.err

def test_main_no_action(capsys):
    with patch('e5_args.list_files_and_directories') as mock_list_files:
        with patch('e5_args.delete_file_or_directory') as mock_delete:
            with patch('e5_args.rename_file_or_directory') as mock_rename:
                with patch('e5_args.search_file_by_name') as mock_search:
                    # Mock the command-line arguments
                    with patch('sys.argv', ['your_script.py', 'path/to/directory']):
                        main()

    # Check if no functions were called
    mock_list_files.assert_not_called()
    mock_delete.assert_not_called()
    mock_rename.assert_not_called()
    mock_search.assert_not_called()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert "No action specified. Use --help for usage instructions" in captured.out

def test_main_help(capsys):
    with patch('e5_args.list_files_and_directories') as mock_list_files:
        with patch('e5_args.delete_file_or_directory') as mock_delete:
            with patch('e5_args.rename_file_or_directory') as mock_rename:
                with patch('e5_args.search_file_by_name') as mock_search:
                    # Mock the command-line arguments
                    with patch('sys.argv', ['your_script.py', '--help']):
                        try:
                            main()
                        except SystemExit as e:
                            # Ignore the SystemExit exception
                            pass

    # Check if no functions were called
    mock_list_files.assert_not_called()
    mock_delete.assert_not_called()
    mock_rename.assert_not_called()
    mock_search.assert_not_called()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert re.sub('\n|[ ]{2,}', ' ','''usage: your_script.py [-h] [--list] [--delete] [--rename RENAME]
                      [--search SEARCH]
                      directory

File and directory manipulation script

positional arguments:
  directory        The target directory for the action

options:
  -h, --help       show this help message and exit
  --list           List files and directories
  --delete         Delete a file or directory
  --rename RENAME  Rename a file or directory
  --search SEARCH  Search for a file by name''') in re.sub('\n|[ ]{2,}', ' ',captured.out.strip())

if __name__ == "__main__":
    pytest.main()
