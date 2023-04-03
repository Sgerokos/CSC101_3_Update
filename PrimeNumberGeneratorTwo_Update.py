# Number of primes to display
NUMBER_OF_PRIMES = 50

# Display 10 per line
NUMBER_OF_PRIMES_PER_LINE = 10

# Count the number of prime numbers
count = 0  

# First number to be tested for primeness
number = 2

print("The first 50 prime numbers are")

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    # Assume the number is prime
    isPrime = True

    # Test if number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
        
            # If true, the number is not prime
            isPrime = False
            break
        divisor += 1

    # Display the prime number and increase the count
    if isPrime:
        count += 1

        print("{0:4}".format(number), end="")
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
        
            # Display the number and advance to the new line
            print()

    # Check the next odd number for primeness
    number += 1
    while number % 2 == 0:
        number += 1