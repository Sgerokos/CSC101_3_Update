import sys

# Request the user to input the three sides of the triangle
a = int(input("Welcome to Triangle Type!"
              "\nPlease enter the length of the first side: "))
b = int(input("\nPlease enter the length of the second side: "))
c = int(input("\nPlease enter the length of the third side: "))

# Check if the triangle sides are positive
if a <= 0 or b <= 0 or c <= 0:
    print("\nInvalid input: Sides must be greater than 0")
    sys.exit()

# Check if the triangle sides can form a valid triangle
if a + b <= c or a + c <= b or b + c <= a:
    print("\nInvalid input: The sides do not form a valid triangle")
    sys.exit()

# If all three sides are equal, the triangle is equilateral
if a == b == c:
    print("\nThis is an equilateral triangle")

# If no sides are equal, the triangle is scalene
elif a != b and a != c and b != c:
    print("\nThis is a scalene triangle")

# If any two sides are equal, the triangle is isosceles
else:
    print("\nThis is an isosceles triangle")