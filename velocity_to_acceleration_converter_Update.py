# Read user inputs for starting and final velocities, and time span
v0 = float(input("Please enter starting velocity (m/s): "))
v1 = float(input("Please enter final velocity (m/s): "))
t = float(input("Please enter time span (s): "))

# Calculate average acceleration using the formula
a = (v1 - v0) / t

# Print the average acceleration for the user
print("The average acceleration is:", a, "m/s^2")