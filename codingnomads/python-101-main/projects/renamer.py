# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

from pathlib import Path
import shutil

desktop_path = Path.home() / "Desktop"

destination_folder = desktop_path / "Renamed_PNGs"
destination_folder.mkdir(exist_ok=True)

png_files = list(desktop_path.glob("*.png"))

for index, png_file in enumerate(png_files, start=1):
    new_name = f"screenshot_{index}.png"
    destination = destination_folder / new_name
    shutil.move(str(png_file), str(destination))
    print(f"Moved {png_file.name} to {destination}")

from pathlib import Path
import shutil

# 1. Find the path to the Desktop
desktop_path = Path.home() / "Desktop"

# 2. Create a new directory named "Renamed_PNGs" on the Desktop
destination_folder = desktop_path / "Renamed_PNGs"
destination_folder.mkdir(exist_ok=True)

# 3. Identify all .png files on the Desktop
png_files = list(desktop_path.glob("*.png"))

# 4. Move and rename each .png file
for index, png_file in enumerate(png_files, start=1):
    new_name = f"screenshot_{index}.png"
    destination = destination_folder / new_name
    shutil.move(str(png_file), str(destination))
    print(f"Moved {png_file.name} to {destination}")