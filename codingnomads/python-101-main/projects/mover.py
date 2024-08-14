# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

from pathlib import Path
import shutil

desktop_path = Path.home() / "Desktop"

destination_folder = desktop_path / "Moved_PNGs"
destination_folder.mkdir(exist_ok=True)

png_files = list(desktop_path.glob("*.png"))

for png_file in png_files:
    destination = destination_folder / png_file.name
    shutil.move(str(png_file), str(destination))
    print(f"Moved {png_file} to {destination}")

from pathlib import Path
import shutil

# 1. Find the path to the Desktop
desktop_path = Path.home() / "Desktop"

# 2. Create a new folder named "Moved_PNGs" on the Desktop
destination_folder = desktop_path / "Moved_PNGs"
destination_folder.mkdir(exist_ok=True)

# 3. Filter for .png files only
png_files = list(desktop_path.glob("*.png"))

# 4. Move each .png file to the new folder
for png_file in png_files:
    destination = destination_folder / png_file.name
    shutil.move(str(png_file), str(destination))
    print(f"Moved {png_file} to {destination}")