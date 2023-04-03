# Import math module
import math

# Calculates the standard deviation of a list of numbers
def deviation(numbers):
    # Calculate the mean of the list
    mean = sum(numbers) / len(numbers)

    # Calculate the variance of the list
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

    # Calculate the standard deviation of the list
    standard_deviation = math.sqrt(variance)

    return standard_deviation

# Calculates the mean of a list of numbers
def mean(numbers):
    # Calculate the sum of the list
    total = sum(numbers)

    # Calculate the mean of the list
    mean = total / len(numbers)

    return mean

# Gets ten numbers from the user and calculates their mean and standard deviation
def main():
    # Prompt the user to enter ten numbers
    user_input = input("Please enter ten digits separated by commas: ")

    # Convert the user's input to a list of floats
    numbers = list(map(float, user_input.split(',')))

    # Calculate the mean and standard deviation of the list
    mean_value = mean(numbers)
    deviation_value = deviation(numbers)

    # Print the mean and standard deviation
    print("\nMean of the following is: {:.2f}".format(mean_value))
    print("\nThe standard deviation is: {:.5f}".format(deviation_value))

# Call the main function
main()