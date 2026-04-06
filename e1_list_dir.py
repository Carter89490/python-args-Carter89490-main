import os

def list_files_and_directories(directory):
    # Check if the directory exists
    exists = os.path.exists(str(directory))
    if exists:
        # List items in the directory
        dir_contents = os.listdir(str(directory))
        for item in dir_contents:
            print(item)
    else:
        print(f"The directory '{directory}' does not exist.")