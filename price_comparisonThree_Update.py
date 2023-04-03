import sys

# Read the input from the user
weight1 = float(input("Enter the weight for package 1: "))
price1 = float(input("Enter the price for package 1: "))
weight2 = float(input("Enter the weight for package 2: "))
price2 = float(input("Enter the price for package 2: "))

# Validate the input
if weight1 <= 0 or price1 <= 0 or weight2 <= 0 or price2 <= 0:
    print("Invalid input. Only positive numbers are accepted.")
    sys.exit()

# Calculate the price per unit weight for each package
price_per_unit_weight1 = price1 / weight1
price_per_unit_weight2 = price2 / weight2

# Compare the prices of the packages
if price_per_unit_weight1 < price_per_unit_weight2:
    print("Package 1 has a better price.")
elif price_per_unit_weight1 > price_per_unit_weight2:
    print("Package 2 has a better price.")
else:
    print("Both packages are equal.")