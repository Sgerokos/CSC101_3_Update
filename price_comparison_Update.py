# Prompt the user to enter the weight and price for two packages
w1 = float(input("Enter the weight for package 1: "))
p1 = float(input("Enter the price for package 1: "))
w2 = float(input("Enter the weight for package 2: "))
p2 = float(input("Enter the price for package 2: "))

# Compare the price per unit weight of both packages
if p1 / w1 > p2 / w2:
    # If the price per unit weight of package 1 is greater than package 2
    # print that package 2 has a better price
    print("Package 2 has a better price.")
else:
    # If the price per unit weight of package 1 is less than or equal to package 2
    # print that package 1 has a better price
    print("Package 1 has a better price.")