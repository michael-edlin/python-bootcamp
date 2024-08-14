# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.


import math

# Define the radius and height of the cylinder
radius = 3.14
height = 5

# Calculate the volume of the cylinder
volume = math.pi * radius**2 * height

# Calculate the surface area of the cylinder
surface_area = 2 * math.pi * radius * (radius + height)

# Print the volume and surface area
print("Volume of the cylinder:", volume)
print("Surface area of the cylinder:", surface_area)