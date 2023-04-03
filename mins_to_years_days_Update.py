# Read the number of minutes from the user
minutes = input("Please enter the number of minutes: ")

# Validate the input to ensure that the user entered a positive integer
while not minutes.isdigit() or int(minutes) <= 0:
    print("Invalid input. Please enter a positive integer.")
    minutes = input("Please enter the number of minutes: ")

# Convert the input to an integer
minutes = int(minutes)

# Calculate the total number of days
days = minutes // (60 * 24)

# Calculate the number of years and days
years = days // 365
remaining_days = days % 365

# Print the result
print("Years:", years, "Days:", remaining_days)