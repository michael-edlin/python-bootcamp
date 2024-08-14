# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

# Step 1: Ask the user to input their name
full_name = input("Please enter your name: ")

# Step 2: Split the name to handle cases where multiple names are entered
first_name = full_name.split()[0]

# Step 3: Print a personalized welcome message using only the first name
print(f"Welcome, {first_name}! I'm glad to have you here.")