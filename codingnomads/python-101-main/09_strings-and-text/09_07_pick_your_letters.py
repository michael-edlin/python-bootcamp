# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
sentence = word[1] + word[2] + " " + word[2] + word[5] + word[5] + " " + word[3] + word[4] + word[5] + word[4] + word[7]
print(sentence)