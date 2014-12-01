# Prints game instructions
def printInstructions():
  printNow(
  """***Welcome to our home!***
  In each room, you will be shown a floor plan of the house.
  You can choose to move some direction by typing north, south,
  east or west.  
  Type help if you want to see the instructions again.
  Type exit if you want to leave the game.  Good luck!""")

# Prints a different message depending on the location
def locationMessage(location):

# Define location messages
  KitchenMessage = """You are now in the kitchen.  You may exit through a door to the west or to the south.
  Come back here to make the pancakes once you have the missing supplies and know how
  many people are home."""
  
  MasterBedroomMessage = """You are now in the master bedroom.  There's nobody in here.  You may exit
  through the door on the east wall or the door on the south wall."""
  
  DiningRoomMessage = """You are now in the dining room.  Someone left the milk on the table, but there's
  no one here now. There are two doors, one on the north wall and one on the west wall."""
  
  LivingRoomMessage = """You are now in the living room.  You see three teenaged boys playing video games
  and shoes everywhere.  You may exit through the door on the north wall or the door on the west wall."""
  
  MattNNicksRoomMessage = """You are now in Matt and Nick's room.  There are several plates on the shelf and
  Nick is still asleep.  Oh wait, there's Collin too, in a sleeping bag on the floor barely
  visible amongst the dirty clothes.  There are two doors, one on the east wall and one on the south wall."""
  
  RyanNJaredsRoomMessage = """You are now in Ryan and Jared's room.  You see Ryan studying for his
  Chemistry test. There is one door on the north wall."""
  
  if location == 'the kitchen':
    printNow(KitchenMessage)
  elif location == 'the masterBedroom':
    printNow(MasterBedroomMessage)
  elif location == 'the dining room':
    printNow(DiningRoomMessage)
  elif location == 'the living room':
    printNow(LivingRoomMessage)
  elif location == 'Matt & Nick\'s room':
    printNow(MattNNicksRoomMessage)
  else:
    printNow(RyanNJaredsRoomMessage)
    
# Requests, validates and stores user input regarding next move
# Possiblemoves = ['north','south','east','west','help','quit']
def getMove():

  return move
  
def changeLocation(location, move):

  return location
# Prints ending message
def finishGame(finished):

# Define ending messages
  QuitMessage = "Tough job, huh? Thanks for trying."
  WinMessage = "You did it! Now you can make pancakes!"
  if finished:
    printNow(QuitMessage)
  else:
    printNow(WinMessage)

def playGame():
# Initialize location and finished variables
  location = "the kitchen"
  finished = false
  
# Print game instructions
  printInstructions()
  
# Game play 
  while not finished:
    locationMessage(location)    
    move = getMove()
    if move == 'quit':
      finished = true
    elif move == help:
      printInstructions()
    else:
      location = changeLocation(location,move)

# Print ending message  
  finishGame(finished)
    

  