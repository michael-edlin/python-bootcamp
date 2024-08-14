# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

# Initialize a counter for vowels
vowel_count = 0

# Define a set of vowels
vowels = "aeiouAEIOU"

# Loop through each character in the text
for char in lorem_ipsum:
    # Check if the character is a vowel
    if char in vowels:
        # If it is, increment the vowel count
        vowel_count += 1

# Print the total number of vowels
print("Total number of vowels:", vowel_count)