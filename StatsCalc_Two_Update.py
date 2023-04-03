# Import math module
import math

# Defines the deviation function
def calculate_standard_deviation(numbers):
    # Call the mean function to get the average of the numbers
    average = calculate_mean(numbers)

    # Get the standard deviation
    variance = math.sqrt((1/len(numbers)) * sum((i - average) ** 2 for i in numbers))

    return variance

# Defines the mean function
def calculate_mean(numbers):
    # Get the average of the numbers
    average = sum(numbers) / len(numbers)

    return average 

# Defines the main method
def main():
    # Ask the user to input ten numbers separated by commas
    numbers = list(map(float, input("Please enter ten numbers separated by commas: ").split(",")))

    # Calculate the standard deviation and mean of the numbers
    standard_deviation = calculate_standard_deviation(numbers)
    mean = calculate_mean(numbers)
    
    # Print the output
    print("\nThe mean is:\n" + str(round(mean, 2))) 
    print("\nThe standard deviation is:\n" + str(round(standard_deviation, 5)))

# Call the main function
main()