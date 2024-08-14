# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

# Step 1: Take a number input from the user
number = int(input("Enter a number between 1 and 1,000,000,000: "))

# Step 2: Check if the number is divisible by 3
if number % 3 == 0:
    print(f"The number {number} is divisible by 3.")
else:
    print(f"The number {number} is not divisible by 3.")