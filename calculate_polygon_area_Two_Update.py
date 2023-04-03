import math, sys

def area(n, s):
    """Evaluates the area of a regular polygon with n sides and side length s."""
    a = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return a

def main():
    """Reads user input for number of sides and side length of a regular polygon,
    calculates the area using the area() function, and prints the result."""
    n = float(input("Please Enter The Number of Sides: "))
    while n <= 1:
        print("Invalid input. Only positive numbers greater than 1 are accepted.")
        n = float(input("Please Enter The Number of Sides: "))
        
    s = float(input("Please Enter The Side: "))
    while s <= 0:
        print("Invalid input. Only positive numbers greater than 0 are accepted.")
        s = float(input("Please Enter The Side: "))
    
    result = area(n, s)
    print("The Area of The Polygon is", result)

main()