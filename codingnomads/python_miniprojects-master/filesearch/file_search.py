# Sentence Analysis Tool
#
# Write a script that takes a sentence from the user and returns:
#
# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.
#
# Note: ignore all spaces.
#
# Example input:
#
# I love to work with dictionaries!
# Example output:
#
# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28

sentence = input("Enter a sentence")

counts = {
    "uppercase": 0,
    "lowercase": 0,
    "punctuation": 0,
    "total_chars": 0
}

for char in sentence:
    if char.isupper():
        counts["uppercase"] += 1
    elif char.islower():
        counts["lowercase"] += 1
    elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
        counts["punctuation"] += 1
    if char != " ":
        counts["total_chars"] += 1

print(f"Upper case: {counts['uppercase']}")
print(f"Lower case: {counts['lowercase']}")
print(f"Punctuation: {counts['punctuation']}")
print(f"Total chars: {counts['total_chars']}")