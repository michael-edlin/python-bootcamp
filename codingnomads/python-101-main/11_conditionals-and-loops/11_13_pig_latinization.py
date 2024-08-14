# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay

import requests

# Step 1: Fetch the story text from the URL
url = "https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt"
response = requests.get(url)
story_text = response.text

# Step 2: Translate the text to Pig Latin
def translate_to_pig_latin(word):
    if len(word) > 1 and word.isalpha():  # Ensures the word has more than 1 letter and is alphabetic
        return word[1:] + word[0] + "ay"
    else:
        return word

translated_story = ""
word = ""

for char in story_text:
    if char.isalpha():  # Part of a word
        word += char
    else:  # Word boundary (space, punctuation, etc.)
        if word:  # If there's a word to translate
            translated_story += translate_to_pig_latin(word)
            word = ""  # Reset the word
        translated_story += char  # Add the punctuation or space as is

# Add any remaining word that hasn't been added
if word:
    translated_story += translate_to_pig_latin(word)

# Print the translated story
print(translated_story)