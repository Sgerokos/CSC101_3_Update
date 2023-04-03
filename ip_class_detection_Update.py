# Function to determine IP address class
def ipClass(ip):
  
  # Split IP address into octets
  octets = ip.split(".")
  
  # Check first octet to determine IP address class
  if 0 <= int(octets[0]) <= 127:
    return "Class A"
  
  elif 128 <= int(octets[0]) <= 191:
    return "Class B"
  
  elif 192 <= int(octets[0]) <= 223:
    return "Class C"
  
  elif 224 <= int(octets[0]) <= 239:
    return "Class D"
  
  elif 240 <= int(octets[0]) <= 255:
    return "Class E"
  
  # If the first octet is out of range, return an error message
  else:
    return "Error: Invalid IP address"


# Main function to get user input and call ipClass function
def main():
  
  # Get user input for IP address
  ip = input("Please enter a valid IP address: ")
  
  # Call ipClass function and print result
  ip_class = ipClass(ip)
  print("IP Address:", ip)
  
  # If the IP address is valid, print the class
  if ip_class != "Error: Invalid IP address":
    print("IP Class:", ip_class)
  
  # If the IP address is invalid, print the error message
  else:
    print(ip_class)
  

# Call the main function
main()