import os
import pytest
from e1_list_dir import list_files_and_directories

# Define a fixture to create a temporary directory for testing
@pytest.fixture
def temp_directory(tmp_path):
    # You can use 'tmp_path' as a pathlib.Path object representing a temporary directory
    return tmp_path

def test_list_files_and_directories_existing_directory(capsys, temp_directory):
    # Create some files and directories in the temporary directory
    temp_directory.joinpath('file1.txt').touch()
    temp_directory.joinpath('file2.txt').touch()
    temp_directory.joinpath('subdirectory').mkdir()

    # Call the function with the temporary directory
    list_files_and_directories(temp_directory)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected items
    assert 'file1.txt' in captured.out
    assert 'file2.txt' in captured.out
    assert 'subdirectory' in captured.out

def test_list_files_and_directories_nonexistent_directory(capsys):
    # Call the function with a nonexistent directory
    list_files_and_directories('/nonexistent_directory')

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert "The directory '/nonexistent_directory' does not exist." in captured.out

if __name__ == "__main__":
    pytest.main()
