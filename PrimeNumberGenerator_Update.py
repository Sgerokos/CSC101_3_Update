# Define the number of prime numbers to display
NUMBER_OF_PRIMES = 50

# Define the number of prime numbers to display per line
NUMBER_OF_PRIMES_PER_LINE = 10

# Initialize the counter for the number of prime numbers found
count = 0

# Ask the user to input a number less than 1000 to start finding prime numbers from
number = int(input("Please enter a number less than 1000 that is not a decimal: "))

# Find the first 50 prime numbers
print("The first 50 prime numbers are:")

# Repeatedly find prime numbers
while number <= 1000:
    # Assume the number is prime
    isPrime = True

    # Test if number is prime by checking if it is divisible by any integer from 2 to number/2
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If the number is divisible by any integer from 2 to number/2, it is not prime
            isPrime = False
            break
        divisor += 1

    # Display the prime number and increase the count if it is prime
    if isPrime:
        count += 1
        print("{0:4}".format(number), end = "")
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to the new line
            print()

    # Check the next number for primality
    number += 1