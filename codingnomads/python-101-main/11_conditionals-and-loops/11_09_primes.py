# Print out every prime number between 1 and 1000.

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Loop through numbers from 1 to 1000
for number in range(1, 1001):
    if is_prime(number):
        print(number)