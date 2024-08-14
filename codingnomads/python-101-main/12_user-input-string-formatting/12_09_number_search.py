# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

# Step 1: Ask the user to input a number between 0 and 1,000,000,000
target_number = int(input("Enter a number between 0 and 1,000,000,000: "))

# Step 2: Initialize a variable to start the loop
current_number = 0

# Step 3: Use a while loop to find the target number
while current_number <= 1_000_000_000:
    if current_number == target_number:
        print(f"The number {current_number} has been found!")
        break  # Exit the loop when the number is found
    current_number += 1  # Increment the number to continue the search