# Imports math module for advanced mathematical operations
import math

# Read the input from the user
n = float(input("Please enter the number of sides: "))
s = float(input("Please enter the side length: "))

# Evaluate the area of a regular polygon using the formula: 
# (n * s^2) / (4 * tan(pi/n))
area = (n * s ** 2) / (4 * math.tan(math.pi / n))

# Print the area of the polygon for the user
print("The area of the regular polygon is", area)