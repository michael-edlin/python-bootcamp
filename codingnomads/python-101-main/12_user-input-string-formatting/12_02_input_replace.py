# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

# Step 1: Get the string of words from the user
string_input = input("Enter a string of words: ")

# Step 2: Get the symbol from the user
symbol_input = input("Enter a symbol to replace the first letter: ")

# Step 3: Identify the first letter
first_letter = string_input[0]

# Step 4: Replace all occurrences of the first letter with the symbol
result = string_input.replace(first_letter, symbol_input)

# Step 5: Display the result
print(f"Result: {result}")