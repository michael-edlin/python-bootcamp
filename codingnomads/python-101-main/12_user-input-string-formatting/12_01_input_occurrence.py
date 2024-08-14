# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

# Step 1: Get the string of words from the user
string_input = input("Enter a string of words: ")

# Step 2: Get the letter to find from the user
letter_input = input("Enter a letter to find its first occurrence: ")

# Step 3: Find the index of the first occurrence of the letter
index = string_input.find(letter_input)

# Step 4: Display the result
if index != -1:
    print(f"Result: {index}")
else:
    print(f"The letter '{letter_input}' is not found in the string.")