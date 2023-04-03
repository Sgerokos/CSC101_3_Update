# Function happy returns the first line of the verse
def happy(): 
  return "If you're happy and you know it," 

# Function clap returns the second line of the verse
def clap(): 
  return "clap your hands (clap clap)" 

# Function face returns the third line of the verse
def face(): 
  return "then your face will surely show it"

# Function stomp returns the fourth line of the verse
def stomp(): 
  return "stomp your feet (stomp stomp)"

# Function shout returns the fifth line of the verse
def shout(): 
  return "shout 'Hurray!' (hoo-ray!)"

# Function doAll returns the sixth line of the verse
def doAll(): 
  return "do all three (clap-clap, stomp-stomp, hoo-ray!)" 

# Print the song 
print(happy(), clap()) 
print(happy(), clap()) 
print(happy(), face()) 
print(happy(), clap(),"\n")
print(happy(), stomp())
print(happy(), stomp())
print(happy(), face())
print(happy(), stomp(), "\n")
print(happy(), shout()) 
print(happy(), shout()) 
print(happy(), face()) 
print(happy(), shout(),"\n") 
print(happy(), doAll()) 
print(happy(), doAll()) 
print(happy(), face()) 
print(happy(), doAll())