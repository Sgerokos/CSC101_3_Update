# Imports modules
import math

# Prompt for the number of sides (must be an integer)
n = int(input("Please enter the number of sides: "))

# Check that n is greater than 0
if n > 0:
    # Prompt for the side length
    s = float(input("Please enter the side length: "))

    # Check that s is greater than 0
    if s > 0:
        # Calculate the area of the polygon
        a = (n * s ** 2) / (4 * math.tan(math.pi / n))

        # Print the result
        print(f"The area of the {n}-sided polygon is {a:.2f}")
    else:
        print("Invalid input: side length must be a positive number.")
        # Alternatively, you could use a try-except block to handle invalid input:
        # try:
        #     s = float(input("Please enter the side length: "))
        # except ValueError:
        #     print("Invalid input: side length must be a number.")
        #     sys.exit()

else:
    print("Invalid input: number of sides must be a positive integer.")
    # Alternatively:
    # try:
    #     n = int(input("Please enter the number of sides: "))
    # except ValueError:
    #     print("Invalid input: number of sides must be an integer.")
    #     sys.exit()

print("Thank you for using the polygon area calculator! Please try again.") 