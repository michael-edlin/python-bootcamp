# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

# Step 1: Take in the values from the user
investment_amount = float(input("Enter the investment amount: "))
interest_rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years to invest: "))

# Step 2: Convert the interest rate to a decimal
interest_rate_decimal = interest_rate / 100

# Step 3: Calculate the future value using the formula: FV = P * (1 + r)^t
future_value = investment_amount * (1 + interest_rate_decimal) ** years

# Step 4: Print the future value to the console
print(f"The future value of your investment is: ${future_value:.2f}")