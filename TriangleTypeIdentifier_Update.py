# Ask the user if they want to continue
triangle = input("Welcome to Triangle Type!!! Please press Y to continue: ")

# Keep asking for triangle sides until the user decides to stop
while triangle == "Y":

    # Request the three sides of the triangle from the user
    a, b, c = eval(input("Please enter the length of the three sides, separated by commas: "))
    
    # Check if the sides form a valid triangle
    if a + b >= c and b + c >= a and c + a >= b:
        
        # Check the type of the triangle based on the side lengths
        if a == b == c:
            print("\nThis is an Equilateral Triangle")
        elif a != b != c != a:
            print("\nThis is a Scalene Triangle")
        else:
            print("\nThis is an Isosceles Triangle")
        
        # Ask the user if they want to input new sides
        triangle = input("Would you like to input new sides? Please press Y for Yes and N for No: ")   
                
    else:
        
        # Notify the user that the given sides do not form a valid triangle
        print("\nThe given sides do not form a triangle.")
        
        # Ask the user if they want to input new sides
        triangle = input("Would you like to input new sides? Please press Y for Yes and N for No: ")
        
# Notify the user that the program has ended
print("Thank you for using Triangle Type!")