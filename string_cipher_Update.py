def encrypt_string(plain_text, cipher):
    """Encrypts a given string using a given cipher."""
    return cipher.join(plain_text)

def decrypt_string(cipher_text, cipher):
    """Decrypts a given string using a given cipher."""
    return cipher_text.split(cipher)

def main():
    """Main program body."""
    # Get the plain text from the user.
    while True:
        plain_text = input("Please enter the text you want to obfuscate: ")
        if plain_text:
            break
        print("Invalid input. Please try again.")

    # Get the cipher key from the user.
    while True:
        cipher_key = input("Please enter the key you want to use to obfuscate: ")
        if cipher_key:
            break
        print("Invalid input. Please try again.")

    # Encrypt the plain text using the cipher key.
    cipher_text = encrypt_string(plain_text, cipher_key)
    print("The encrypted string is:", cipher_text)

    # Decrypt the cipher text using the cipher key.
    plain_text_again = ''.join(decrypt_string(cipher_text, cipher_key))
    print("The decrypted string is:", plain_text_again)

if __name__ == '__main__':
    main()