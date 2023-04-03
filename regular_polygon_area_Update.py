# Import modules
import math
import sys

def area(n, s):
    """
    Computes the area of a regular polygon with given number of sides and side length.

    Args:
    n (float): number of sides of the polygon
    s (float): length of a side of the polygon

    Returns:
    None
    """
    a = (n * s ** 2) / (4 * math.tan(math.pi / n))
    # Print the area of the polygon for the user
    print("The area of the polygon is", a)    
    
# Read input from the user
n = float(input("Please enter the number of sides: "))
# If n equals 0 or less than 0 system exit
if n <= 0:
    print("Improper input. Only positive integers greater than 1 are accepted.")
    sys.exit()  
# Read input from the user
s = float(input("Please enter the side length: "))
# If s equals 0 or less than 0 system exit
if s <= 0:
    print("Improper input. Only positive integers greater than 1 are accepted.")
    sys.exit() 

area(n,s)