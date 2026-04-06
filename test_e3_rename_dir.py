import os
import pytest
from e3_rename_dir import rename_file_or_directory

# Define a fixture to create a temporary directory and file for testing
@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path.joinpath('test_file.txt')
    file_path.touch()
    return file_path

def test_rename_file(temp_file, capsys):
    file_path = temp_file

    # Define the new name for the file
    new_name = 'renamed_file.txt'

    # Call the function to rename the file
    rename_file_or_directory(file_path, new_name)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert f"Renamed '{file_path}' to '{os.path.join(os.path.dirname(file_path), new_name)}'." in captured.out

    # Check if the file has been renamed
    assert not os.path.exists(file_path)
    assert os.path.exists(os.path.join(os.path.dirname(file_path), new_name))

def test_rename_nonexistent_file(capsys):
    # Call the function with a nonexistent file path
    rename_file_or_directory('/nonexistent_file.txt', 'new_name')

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the output contains the expected message
    assert "The file or directory '/nonexistent_file.txt' does not exist." in captured.out

if __name__ == "__main__":
    pytest.main()
