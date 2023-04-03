# Prompt the user to enter the number of minutes
minutes = int(input("Please enter the number of minutes: "))

# Calculate the total number of days based on the input minutes
total_days = (minutes / 60) / 24

# Calculate the number of years and days from the total days
years = int(total_days / 365)
days = int(total_days % 365)

# Print the results for the user
print("Years:", years, "Days:", days)