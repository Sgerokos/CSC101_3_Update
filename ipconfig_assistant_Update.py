# Imports the required modules
import subprocess
import sys

# Requests the user to select one of the following
ip = input("Please Enter One of The Following: " 
             "\n1 for ipconfig," 
             "\n2 for ipconfig /all,"
             "\n3 for ipconfig /renew," 
             "\n4 for ipconfig /renew EL*," 
             "\n5 for ipconfig /release *Con*,"
             "\n6 for ipconfig /allcompartments," 
             "\n7 for ipconfig /allcompartments /all," 
             "\nor help for Assistance in Choosing: ")

# If help is entered list's the algorithms and what they are
if ip == "help":
    
    print("\n1. ipconfig: Shows information on IP configuration."
          "\n2. ipconfig /all: Shows detailed information on IP configuration."
          "\n3. ipconfig /renew: Renews all adapters."
          "\n4. ipconfig /renew EL*: Renews any connection that has its name starting with EL."
          "\n5. ipconfig /release *Con*: Releases all matching connections (e.g. Wired Ethernet Connection 1, Wired Ethernet Connection 2)."
          "\n6. ipconfig /allcompartments: Shows information about all compartments."
          "\n7. ipconfig /allcompartments /all: Shows detailed information about all compartments.\n")
    
    # Re-ask the user to select one of the options
    ip = input("Please Re-Enter One of The Following." 
               "\n1 for ipconfig," 
               "\n2 for ipconfig /all,"
               "\n3 for ipconfig /renew," 
               "\n4 for ipconfig /renew EL*," 
               "\n5 for ipconfig /release *Con*,"
               "\n6 for ipconfig /allcompartments," 
               "\n7 for ipconfig /allcompartments /all," 
               "\nor help for Assistance in Choosing:" )

# Execute the chosen ipconfig command
if ip == "1":
    subprocess.call("ipconfig",shell=True)
    
elif ip == "2":
    subprocess.call("ipconfig /all",shell=True)

elif ip == "3":
    subprocess.call("ipconfig /renew",shell=True)
    
elif ip == "4":
    subprocess.call("ipconfig /renew EL*",shell=True)
    
elif ip == "5":
    subprocess.call("ipconfig /release *Con*",shell=True)

elif ip == "6":
    subprocess.call("ipconfig /allcompartments",shell=True)
    
elif ip == "7":
    subprocess.call("ipconfig /allcompartments /all",shell=True)    

else:
    print("\n\nSorry Wrong Input." 
        "\nPlease Try Again." 
        "\nNow Exiting!!!")
    sys.exit()