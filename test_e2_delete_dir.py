import os
import pytest
from e2_delete_dir import delete_file_or_directory

# Define a fixture to create a temporary directory and file for testing
@pytest.fixture
def temp_file_and_directory(tmp_path):
    file_path = tmp_path.joinpath('test_file.txt')
    file_path.touch()

    directory_path = tmp_path.joinpath('test_directory')
    directory_path.mkdir()

    return file_path, directory_path

def test_delete_file(temp_file_and_directory, capsys):
    file_path, _ = temp_file_and_directory

    # Call the function with the temporary file
    delete_file_or_directory(file_path)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert f"File '{file_path}' has been deleted." in captured.out

    # Check if the file has been deleted
    assert not os.path.exists(file_path)

def test_delete_directory(temp_file_and_directory, capsys):
    _, directory_path = temp_file_and_directory

    # Call the function with the temporary directory
    delete_file_or_directory(directory_path)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert f"Directory '{directory_path}' has been deleted." in captured.out

    # Check if the directory has been deleted
    assert not os.path.exists(directory_path)

def test_delete_nonexistent_file_or_directory(capsys):
    # Call the function with a nonexistent path
    delete_file_or_directory('/nonexistent_path')

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert "The file or directory '/nonexistent_path' does not exist." in captured.out

if __name__ == "__main__":
    pytest.main()
