import os
import pytest
from e4_search_dir import search_file_by_name

# Define a fixture to create a temporary directory and file for testing
@pytest.fixture
def temp_file_and_directory(tmp_path):
    file_path = tmp_path.joinpath('test_file.txt')
    file_path.touch()
    return file_path

def test_search_file_by_name_existing_file(temp_file_and_directory, capsys):
    file_path = temp_file_and_directory
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)

    # Call the function to search for the existing file
    search_file_by_name(directory, filename)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert f"File '{filename}' found in '{directory}'." in captured.out

def test_search_file_by_name_nonexistent_file(temp_file_and_directory, capsys):
    file_path = temp_file_and_directory
    directory = os.path.dirname(file_path)
    # Call the function with a nonexistent filename
    search_file_by_name(directory, 'nonexistent_file.txt')

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert f"File 'nonexistent_file.txt' not found in '{directory}" in captured.out

def test_search_file_by_name_nonexistent_directory(capsys):
    # Call the function with a nonexistent directory
    search_file_by_name('/nonexistent_directory', 'test_file.txt')

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert "The directory '/nonexistent_directory' does not exist." in captured.out
