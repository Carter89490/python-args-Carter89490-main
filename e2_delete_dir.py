import os
import shutil

def delete_file_or_directory(path):
    try:
        # Check if the file or directory exists
        exists = os.path.exists(str(path))
        if exists:
            # Check if the path is a file or directory
            is_file = os.path.isfile(str(path))
            is_dir = os.path.isdir(str(path))
            if is_file:
                # Delete the file
                os.remove(str(path))
                print(f"File '{path}' has been deleted.")
            elif is_dir:
                # Delete the directory
                shutil.rmtree(str(path))
                print(f"Directory '{path}' has been deleted.")
        else:
            print(f"The file or directory '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")