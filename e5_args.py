from e1_list_dir import list_files_and_directories
from e2_delete_dir import delete_file_or_directory
from e3_rename_dir import rename_file_or_directory
from e4_search_dir import search_file_by_name
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="your_script.py",
        description="File and directory manipulation script"
    )
    parser.add_argument("directory", help="The target directory for the action")
    parser.add_argument("--list", action="store_true", help="List files and directories")
    parser.add_argument("--delete", action="store_true", help="Delete a file or directory")
    parser.add_argument("--rename", help="Rename a file or directory")
    parser.add_argument("--search", help="Search for a file by name")

    args = parser.parse_args()

    is_list = args.list
    is_delete = args.delete
    is_rename = args.rename
    is_search = args.search

    if is_list:
        list_files_and_directories(args.directory)
    elif is_delete:
        delete_file_or_directory(args.directory)
    elif is_rename:
        rename_file_or_directory(args.directory, args.rename)
    elif is_search:
        search_file_by_name(args.directory, args.search)
    else:
        print("No action specified. Use --help for usage instructions")

if __name__ == "__main__":
    main()