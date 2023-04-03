# Imports the required modules
import subprocess
import sys

def main():
    # Show the menu and get the user's choice
    user_choice = get_user_choice()

    # Execute the chosen ipconfig command
    execute_ipconfig_command(user_choice)

def get_user_choice():
    while True:
        choice = input("Please enter one of the following:"
                       "\n1 for ipconfig,"
                       "\n2 for ipconfig /all,"
                       "\n3 for ipconfig /renew,"
                       "\n4 for ipconfig /renew EL*,"
                       "\n5 for ipconfig /release *Con*,"
                       "\n6 for ipconfig /allcompartments,"
                       "\n7 for ipconfig /allcompartments /all,"
                       "\nor help for assistance in choosing: ")

        if choice == "help":
            print_help_message()
        else:
            return choice

def print_help_message():
    print("\n1. ipconfig: Shows information on IP configuration."
          "\n2. ipconfig /all: Shows detailed information on IP configuration."
          "\n3. ipconfig /renew: Renews all adapters."
          "\n4. ipconfig /renew EL*: Renews any connection that has its name starting with EL."
          "\n5. ipconfig /release *Con*: Releases all matching connections (e.g. Wired Ethernet Connection 1, Wired Ethernet Connection 2)."
          "\n6. ipconfig /allcompartments: Shows information about all compartments."
          "\n7. ipconfig /allcompartments /all: Shows detailed information about all compartments.\n")

def execute_ipconfig_command(choice):
    commands = {
        "1": "ipconfig",
        "2": "ipconfig /all",
        "3": "ipconfig /renew",
        "4": "ipconfig /renew EL*",
        "5": "ipconfig /release *Con*",
        "6": "ipconfig /allcompartments",
        "7": "ipconfig /allcompartments /all"
    }

    if choice in commands:
        subprocess.call(commands[choice], shell=True)
    else:
        print("\n\nSorry, wrong input."
              "\nPlease try again."
              "\nNow exiting!!!")
        sys.exit()

if __name__ == "__main__":
    main()