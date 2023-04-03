# Imports modules
import math
import sys

while True:
    # Get the number of sides from the user
    num_sides = input("Please enter the number of sides (must be a positive integer): ")
    try:
        num_sides = int(num_sides)
        if num_sides <= 0:
            print("Error: number of sides must be a positive integer.")
            continue
    except ValueError:
        print("Error: invalid input. Please enter a positive integer.")
        continue

    # Get the length of each side from the user
    side_length = input("Please enter the length of each side (must be a positive number): ")
    try:
        side_length = float(side_length)
        if side_length <= 0:
            print("Error: side length must be a positive number.")
            continue
    except ValueError:
        print("Error: invalid input. Please enter a positive number.")
        continue

    # Calculate the area of the regular polygon
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

    # Print the result
    print(f"The area of the regular polygon with {num_sides} sides and side length {side_length} is {area}.")

    # Ask the user if they want to calculate another area
    choice = input("Do you want to calculate the area of another regular polygon? (y/n) ")
    if choice.lower() != "y":
        break

print("Thank you for using the regular polygon area calculator!")