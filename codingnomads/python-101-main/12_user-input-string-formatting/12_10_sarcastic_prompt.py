# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.


def alternating_caps(text):
    # Initialize an empty string to hold the result
    result = ""

    # Variable to track if we need an uppercase or lowercase letter
    uppercase = True

    # Loop through each character in the input text
    for char in text:
        if char.isalpha():  # Only change case if the character is a letter
            if uppercase:
                result += char.upper()
            else:
                result += char.lower()
            # Toggle the uppercase flag
            uppercase = not uppercase
        else:
            result += char  # Add the character as it is if it's not a letter

    return result

# Ask the user for their honest opinion
user_input = input("What's your honest opinion? ")

# Print the sarcastic response
sarcastic_response = alternating_caps(user_input)
print(sarcastic_response)