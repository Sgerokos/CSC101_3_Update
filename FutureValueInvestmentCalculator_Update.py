# Read the input from the user
investment_amount = float(input("Please enter the amount you would like to invest: "))
annual_interest_rate = float(input("Please enter the annual interest rate (as a percentage): ")) / 12
investment_duration_years = int(input("Please enter the investment duration (in years): "))

# Convert the investment duration to months
investment_duration_months = investment_duration_years * 12

# Calculate the future investment value
future_value = investment_amount * (1 + annual_interest_rate / 100) ** investment_duration_months

# Print the result for the user
print("The accumulated value after", investment_duration_years, "years is:", round(future_value, 2))