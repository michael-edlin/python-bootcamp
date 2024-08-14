# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

# Step 1: Take three string inputs from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string3 = input("Enter the third string: ")

# Step 2: Create a list of the strings
strings = [string1, string2, string3]

# Step 3: Find the longest string using max() with key=len
longest_string = max(strings, key=len)

# Step 4: Print the length of the longest string and the string itself
print(f"{len(longest_string)}, {longest_string}")