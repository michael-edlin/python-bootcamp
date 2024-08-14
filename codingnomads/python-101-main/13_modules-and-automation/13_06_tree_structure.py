# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import os

def find_python_files(directory):
    print(f"Searching for Python files in: {directory}\n")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                print(f"Found: {full_path}")

    print("\nSearch complete.")

if __name__ == "__main__":
    # Set the directory you want to search in. Replace 'labs_folder' with the path to your labs folder.
    labs_folder = "/path/to/your/labs_folder"  # Replace with the path to your labs folder
    find_python_files(labs_folder)