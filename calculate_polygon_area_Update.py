import math
import sys

def area(n, s):
    """
    Calculate the area of a regular polygon using its number of sides and side length.

    Args:
    n (float): number of sides of the polygon
    s (float): length of one side of the polygon

    Returns:
    float: the calculated area of the polygon
    """
    a = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return a
    
# Get user input for number of sides and side length
n = float(input("Please Enter The Number of Sides: "))
if n <= 0:
    print("Invalid input. Only positive integers greater than 0 are accepted.")
    sys.exit()  
    
s = float(input("Please Enter The Side: "))
if s <= 0:
    print("Invalid input. Only positive integers greater than 0 are accepted.")
    sys.exit() 

# Calculate and print the area of the polygon
result = area(n, s)
print("The Area of The Polygon is", result)