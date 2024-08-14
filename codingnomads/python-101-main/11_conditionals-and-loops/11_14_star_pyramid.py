# Write a script that prints a star pyramid of flexible size
# If the `stars` variable is `5`, your code will output:
#
# *
# * *
# * * * 
# * * * *
# * * * * * 
#
# There should be five rows in total:
# 1. the 1st row will have 1 star,
# 2. the 2nd row will have 2 stars,
# 3. the 3rd row will have 3 stars,
# 4. the 4th row will have 4 stars,
# 5. the 5th row will have 5 stars
#
# Another example: if you set the `stars` variable tp `3`, 
# your code will output:
#
# *
# * *
# * * *
#
# HINT: Think of nested for loops!

# Step 1: Set the variable `stars`
stars = 5  # You can change this to any number for different pyramid sizes

# Step 2: Create the star pyramid using nested loops
for i in range(1, stars + 1):  # Outer loop for the rows
    for j in range(i):  # Inner loop for printing stars
        print("*", end=" ")  # Print star and stay on the same line
    print()  # Move to the next line after each row