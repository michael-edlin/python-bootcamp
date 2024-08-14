# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

from pathlib import Path

def find_jpg_files(folder):
    # Convert the folder path to a Path object
    folder_path = Path(folder)

    # Initialize an empty list to hold the paths of .jpg files
    jpg_files = []

    # Iterate through the folder and its subfolders up to two levels deep
    for path in folder_path.glob('**/*.jpg'):
        # Add the complete path of each .jpg file to the list
        jpg_files.append(str(path.resolve()))

    return jpg_files

def find_all_file_types(folder):
    # Convert the folder path to a Path object
    folder_path = Path(folder)

    # Initialize an empty dictionary to hold file extensions and their paths
    file_types = {}

    # Iterate through the folder and its subfolders up to two levels deep
    for path in folder_path.glob('**/*'):
        if path.is_file():
            # Get the file extension
            ext = path.suffix.lower()
            # Add the path to the corresponding extension in the dictionary
            if ext not in file_types:
                file_types[ext] = []
            file_types[ext].append(str(path.resolve()))

    return file_types

if __name__ == "__main__":
    # Specify the folder you want to search
    folder_to_search = '/path/to/your/folder'

    # Find all .jpg files in the specified folder and its subfolders
    jpg_files = find_jpg_files(folder_to_search)
    print("List of .jpg files:")
    for file in jpg_files:
        print(file)

    # Find all file types in the specified folder and its subfolders
    all_file_types = find_all_file_types(folder_to_search)
    print("\nList of all file types found:")
    for ext, files in all_file_types.items():
        print(f"\n{ext} files:")
        for file in files:
            print(file)