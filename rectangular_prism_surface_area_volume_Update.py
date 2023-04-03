# Reads the input from the user
# and assigns it to variables
l = float(input("Please Enter The Rectangular Prism Length: "))
h = float(input("Please Enter The Rectangular Prism Height: "))
w = float(input("Please Enter The Rectangular Prism Width: "))

# Calculates the surface area of the rectangular prism 
sa = 2 * ((l * h) + (w * h) + (l * w))  

# Calculates the volume of the rectangular prism 
v = l * h * w

# Prints the surface area and the volume 
# of the rectangular prism for the user to see
print("Surface Area is:", sa, "Volume is:", v)