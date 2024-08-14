# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

# 1) Convert an int to a float
int_value = 10
float_value = float(int_value)
print("Int to Float:", float_value)  # Output: 10.0

# 2) Convert a float to an int
float_value = 10.7
int_value = int(float_value)
print("Float to Int:", int_value)  # Output: 10

# 3) Perform division using a float and an int
result = float_value / int_value
print("Division of Float by Int:", result)  # Output: 1.07

# 4) Use two variables to perform a multiplication
a = 5
b = 3.2
multiplication_result = a * b
print("Multiplication Result:", multiplication_result)  # Output: 16.0

# When you convert a float to an int, the decimal part is lost (e.g., 10.7 becomes 10). This is a loss of precision.