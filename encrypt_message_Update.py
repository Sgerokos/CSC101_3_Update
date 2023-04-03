# Defines the function encrypt
def encrypt(s, key):
    """Encrypts the given string with the provided key using a join operation"""
    return key.join(s)

# Defines the main function
def main():
    """Main function that prompts the user for input and calls the encrypt function"""

    # Request input from the user
    txt = input("Please enter the text you want to encrypt: \n")
    key = input("\nPlease enter the key you want to use to encrypt: \n")

    # Encrypt the input using the provided key
    encrypted_text = encrypt(txt, key)

    # Print the input, key, and encrypted text to the console
    print("\nThe original text is: \n" + txt, 
          "\n\nThe key used for encryption is: \n" + key, 
          "\n\nThe encrypted text is: \n" + encrypted_text)

# Call the main function to start the program
main()