# Read the investment details from the user
investment_amount = float(input("Please Enter The Amount You Would Want to Invest: "))
annual_interest_rate = float(input("Please Enter The Annual Interest Rate (in percentage): ")) / 12
years = int(input("Enter Number of Year's: "))

# Calculate the future investment value
total_months = years * 12
future_value = investment_amount * (1 + annual_interest_rate / 100) ** total_months

# Print the accumulated value for the user
print("The Accumulated Value after {} years is ${:,.2f}".format(years, future_value))

# Ask the user if they want to perform another calculation
answer = input("Do you want to perform another calculation? (Y/N) ")

while answer.lower() == "y":
    # Read the investment details from the user
    investment_amount = float(input("Please Enter The Amount You Would Want to Invest: "))
    annual_interest_rate = float(input("Please Enter The Annual Interest Rate (in percentage): ")) / 12
    years = int(input("Enter Number of Year's: "))

    # Calculate the future investment value
    total_months = years * 12
    future_value = investment_amount * (1 + annual_interest_rate / 100) ** total_months

    # Print the accumulated value for the user
    print("The Accumulated Value after {} years is ${:,.2f}".format(years, future_value))

    # Ask the user if they want to perform another calculation
    answer = input("Do you want to perform another calculation? (Y/N) ")