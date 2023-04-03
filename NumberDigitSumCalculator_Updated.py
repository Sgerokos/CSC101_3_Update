# Prompt the user to enter a number between 0 and 1000
n = -1
while n < 0 or n > 1000:
    n = int(input("Please Enter A Number Between 0 And 1000: "))

# Extract the digits of the number using the modulus operator
d = n % 10
c = (n // 10) % 10
b = (n // 100) % 10
a = (n // 1000) % 10

# Calculate the sum of the digits
digit_sum = a + b + c + d

# Print the result for the user
print("The Sum Of All The Digits In The Number is", digit_sum)