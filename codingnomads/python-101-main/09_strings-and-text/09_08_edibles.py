# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

# Extract the word "grappled"
food1 = s[5:13]

# Extract the word "leggin" (similar to 'legume', though not a perfect match, let's consider it as a play on words)
food2 = s[30:36]

# Extract the word "butter"
food3 = s[54:60]

# Extract the word "cups" (as in 'buttercup')
food4 = s[60:64]

print(food1, food2, food3, food4)