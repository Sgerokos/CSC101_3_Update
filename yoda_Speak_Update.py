def yoda_speak(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Rearrange the words according to Yoda's speech pattern
    yoda_order = words[2:] + words[:2]

    # Join the rearranged words to form a Yodish sentence
    yodish = " ".join(yoda_order)

    return yodish

def main():
    # Ask for user input
    user_input = input("Please enter a sentence"
                       "\nthat you would like to convert to Yodish: \n\n")

    # Convert the sentence to Yodish
    yodish_sentence = yoda_speak(user_input)

    # Print the Yodish sentence
    print("\nYodish form:")
    print(yodish_sentence)

main()