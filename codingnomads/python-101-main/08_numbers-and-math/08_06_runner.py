# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

# Define the variables
miles_run = 10
time_minutes = 30
time_seconds = 30
mile_to_km = 1.6

# Convert miles to kilometers
kilometers_run = miles_run * mile_to_km

# Convert the time to hours
time_in_hours = time_minutes / 60 + time_seconds / 3600

# Calculate the average speed in km/h
average_speed = kilometers_run / time_in_hours

# Print the result
print("Average speed in kilometers per hour:", average_speed)