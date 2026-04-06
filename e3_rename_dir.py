import os

def rename_file_or_directory(old_path, new_name):
    try:
        # Check if the file or directory exists
        exists = os.path.exists(str(old_path))
        if exists:
            # Get the directory of the old path and join it to the new name
            new_path = os.path.join(os.path.dirname(str(old_path)), new_name)
            # Rename the file or directory
            os.rename(str(old_path), new_path)
            print(f"Renamed '{old_path}' to '{new_path}'.")
        else:
            print(f"The file or directory '{old_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")