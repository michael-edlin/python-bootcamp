# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

for i in range(0, 50):
    if i % 10 == 0 and i != 0:
        print()  # Start a new line after every 10 numbers
    print(f"{i:2}", end=" ")  # Print each number with a width of 2 characters

print()  # Add a newline at the end of the output