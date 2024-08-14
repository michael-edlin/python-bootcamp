# Think about a task that you want to accomplish using programming
# Maybe you want to automate something you do every day on your computer?
# Break down some of the steps you can think of and write them in
# this file as pseudocode.
# You can come back and update this file when you've learned more.
# You can also add real Python code after learning the necessary concepts.
# For now, just practice breaking larger tasks into smaller steps
# and writing out your thoughts in pseudocode.

# Step 1: Define the path to the folder
folder_path = "/path/to/your/folder"

# Step 2: Loop through files in the folder
for file in os.listdir(folder_path):
    # Step 3: Check the file extension
    if file.endswith(".txt"):
        # Step 4: Create a 'TextFiles' folder if it doesn't exist
        if not os.path.exists(folder_path + "/TextFiles"):
            os.mkdir(folder_path + "/TextFiles")
        # Step 5: Move the file to 'TextFiles'
        shutil.move(file, folder_path + "/TextFiles")
    # Repeat for other file types like .jpg, .pdf, etc.

# Step 6: Handle exceptions (to be elaborated)
# Step 7: Print completion message
print("Files organized successfully!")