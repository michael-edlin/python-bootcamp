# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

# Step 1: Take a string input from the user
user_input = input("Enter a string: ").lower()

# Step 2: Initialize a dictionary to hold the counts of each vowel
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Step 3: Loop through each character in the string
for char in user_input:
    # Step 4: Check if the character is a vowel, and if so, increment its count
    if char in vowel_counts:
        vowel_counts[char] += 1

# Step 5: Print the counts of each vowel
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")