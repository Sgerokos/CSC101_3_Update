# Import the random module
import random

# Set the number of trials for estimating PI
NUMBER_OF_TRIALS = 1000000

# Initialize a variable to keep track of the number of hits
numberOfHits = 0

# Loop over the number of trials
for i in range(NUMBER_OF_TRIALS):
    # Generate a random x-coordinate between -1 and 1
    x = random.random() * 2 - 1
    # Generate a random y-coordinate between -1 and 1
    y = random.random() * 2 - 1

    # Check if the point is inside the unit circle
    if x * x + y * y <= 1:
        # Increment the number of hits if the point is inside the circle
        numberOfHits += 1
        
# Estimate PI using the ratio of hits to total trials
pi = 4 * numberOfHits / NUMBER_OF_TRIALS

# Print the estimated value of PI
print("PI is", pi)