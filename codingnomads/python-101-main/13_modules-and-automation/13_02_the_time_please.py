# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print the current date and time in a readable format
print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))