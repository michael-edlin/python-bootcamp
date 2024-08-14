# Fix the wikipedia blurb below by replacing the value for `animal`
# with the name of the animal that the text is talking about.
# Then, change the that way you're displaying the multi-line string
# so that the output doesn't show any superfluous spacing.

# Assign the correct animal name to the variable
animal = "cat"

# Create the blurb without any unnecessary spacing
blurb = (
    f"The {animal} (Felis {animal}us) is a domestic species of small "
    f"carnivorous mammal. It is the only domesti{animal}ed species "
    f"in the family Felidae and is often referred to as the "
    f"domestic {animal} to distinguish it from the wild members of the family."
)

# Print the blurb
print(blurb)