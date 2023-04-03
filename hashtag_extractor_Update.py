# Defines the hashtag extractor function
def hashtag_extractor(user_input):
    """
    Extracts hashtags from a given string.

    Args:
        user_input (str): The input string to extract hashtags from.

    Returns:
        A tuple containing the message "Hashtags Found:" and a string
        containing the hashtags found, separated by spaces.
    """
    hashtags = [word for word in user_input.split() if word.startswith("#")]
    return "Hashtags Found:", ' '.join(hashtags)


# Defines the mentions extractor function
def mentions_extractor(user_input):
    """
    Extracts mentions from a given string.

    Args:
        user_input (str): The input string to extract mentions from.

    Returns:
        A tuple containing the message "Mentions Found:" and a string
        containing the mentions found, separated by spaces.
    """
    mentions = [word for word in user_input.split() if word.startswith("@")]
    return "Mentions Found:", ' '.join(mentions)


# Defines the main function
def main():
    # Example input for testing
    user_input = "learn #cplusplus from @ATT and #java from @Oracle and #Python from @ThePSF"

    # Print the found hashtags and mentions
    print(*hashtag_extractor(user_input), "\n")
    print(*mentions_extractor(user_input))


# Call the main function
main()