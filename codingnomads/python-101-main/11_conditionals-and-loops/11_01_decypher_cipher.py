# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""

# Loop through each character in the secret string
for char in secret:
    # Check if the character is alphabetic
    if char.isalpha():
        # If it is, add it to the solution
        solution += char

# Print the deciphered message
print(solution)
