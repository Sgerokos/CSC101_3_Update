# Prompt the user to enter weights and prices for two packages
weight_1 = float(input("Enter the weight for package 1: "))
price_1 = float(input("Enter the price for package 1: "))
weight_2 = float(input("Enter the weight for package 2: "))
price_2 = float(input("Enter the price for package 2: "))

# Compare the price per unit weight for the two packages
if price_1 / weight_1 > price_2 / weight_2:
    print("Package 2 has a better price.")
else:
    print("Package 1 has a better price.")