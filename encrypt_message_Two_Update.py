# Imports random module
import random

def obfuscate(key):
    """
    Generate a random string of characters with a given length.

    Args:
    - key: an integer representing the length of the string to generate

    Returns:
    - a random string of characters with the given length
    """
    return ''.join(chr(random.randint(33, 127)) for _ in range(key))

def encryption(txt, key):
    """
    Encrypt a given string with a given key using the obfuscate function.

    Args:
    - txt: a string to encrypt
    - key: an integer representing the length of the obfuscation key

    Returns:
    - a string representing the encrypted text
    """
    return ''.join(c + obfuscate(key) for c in txt)

def main():
    """
    Prompt the user for a string to encrypt and a key length, then print the
    encrypted string.
    """
    txt = input("Please enter the text you want to obfuscate: ")
    key = int(input("Please enter the key length: "))
    encrypted = encryption(txt, key)
    print(f"\nThe text is:\n{txt}\n\nThe key length is:\n{key}\n\nThe obfuscated string is:\n{encrypted}")

main()