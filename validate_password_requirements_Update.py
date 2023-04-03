# Defines the function has_min_length
def has_min_length(password):
    # Checks if the password is at least 8 characters or more
    return len(password) >= 8

# Defines the function has_digits
def has_digits(password):
    # Checks if the password contains digits
    return any(char.isdigit() for char in password)

# Defines the function has_uppercase
def has_uppercase(password):
    # Checks if the password contains an uppercase letter
    return any(char.isupper() for char in password)

# Defines the function has_lowercase
def has_lowercase(password):
    # Checks if the password contains a lowercase letter
    return any(char.islower() for char in password)

# Defines the function has_symbols
def has_symbols(password):
    # Checks if the password contains a special symbol
    symbols = "!@#$%^&*()+="
    return any(char in symbols for char in password)

# Defines the function passwordCheck
def passwordCheck(password):
    # Checks if the password meets all the requirements
    if not has_min_length(password):
        return "Password must be at least 8 characters long."
    elif not has_digits(password):
        return "Password must contain at least one digit."
    elif not has_uppercase(password):
        return "Password must contain at least one uppercase letter."
    elif not has_lowercase(password):
        return "Password must contain at least one lowercase letter."
    elif not has_symbols(password):
        return "Password must contain at least one special symbol."
    else:
        return "The password is valid."

# Defines the function main
def main():
    # Prompts the user to enter a password
    password = input("Please enter a password that meets the following requirements:\n"
                     "- At least 8 characters long\n"
                     "- Contains at least one digit\n"
                     "- Contains at least one uppercase letter\n"
                     "- Contains at least one lowercase letter\n"
                     "- Contains at least one special symbol (!@#$%^&*()+=)\n\n"
                     "Password: ")

    # Checks if the password is valid
    result = passwordCheck(password)

    # Prints the result
    print(result)
    if result == "The password is valid.":
        print("You have successfully created a strong password!")

# Calls the main function
main()