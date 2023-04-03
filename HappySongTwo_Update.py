# First function happy
def happy(): 
  """Return the first line of the song."""
  return "If you're happy and you know it," 

# Second function clap
def clap(): 
  """Return the second line of the song."""
  return "clap your hands (clap clap)" 

# Third function face
def face(): 
  """Return the third line of the song."""
  return "then your face will surely show it"

# Fourth function stomp
def stomp(): 
  """Return the fourth line of the song."""
  return "stomp your feet (stomp stomp)"

# Fifth function shout
def shout(): 
  """Return the fifth line of the song."""
  return 'shout "Hurray!" (hoo-ray!)'

# Sixth function doAll
def doAll(): 
  """Return the sixth line of the song."""
  return 'do all three (clap-clap, stomp-stomp, hoo-ray!)'

def print_if_youre_happy_and_you_know_it_lyrics():
  """Print the lyrics of the song 'If You're Happy and You Know It'."""
  # Print the song
  print(f"{happy()} {clap()}") 
  print(f"{happy()} {clap()}") 
  print(f"{happy()} {face()}") 
  print(f"{happy()} {clap()}\n")
  print(f"{happy()} {stomp()}")
  print(f"{happy()} {stomp()}")
  print(f"{happy()} {face()}")
  print(f"{happy()} {stomp()}\n")
  print(f"{happy()} {shout()}") 
  print(f"{happy()} {shout()}") 
  print(f"{happy()} {face()}") 
  print(f"{happy()} {shout()}\n") 
  print(f"{happy()} {doAll()}") 
  print(f"{happy()} {doAll()}") 
  print(f"{happy()} {face()}") 
  print(f"{happy()} {doAll()}")

# Call the function to print the lyrics of the song
print_if_youre_happy_and_you_know_it_lyrics()