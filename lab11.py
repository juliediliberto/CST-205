# Prints game instructions
def printInstructions():
  printNow(
  """***Welcome to our home!***
  In each room, you will be shown a floor plan of the house.
  You can choose to move some direction by typing north, south,
  east or west.  
  Type help if you want to see the instructions again.
  Type quit if you want to leave the game.  Good luck!""")

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
  
  NotAllowed = """Sorry, You are not allowed to move in that direction."""
  
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
  elif location == 'Ryan & Jared\'s room':
    printNow(RyanNJaredsRoomMessage)
  elif location == 'not allowed':
    printNow(NotAllowed)
  else:
    printNow("Direction Undefined")
    
# Requests, validates and stores user input regarding next move
# Possiblemoves = ['north','south','east','west','help','quit']
def getMove():
  move = requestString("What direction would you like to go in?\nType help for instructions of quit to exit the game.")  
  if move == "help":
    return 'help'
  elif move == "quit":
    return 'quit'
  elif move == "north" or move == "n":
    return 'north'
  elif move == "south" or move == "s":
    return 'south'
  elif move == "east" or move == "e":
    return 'east'
  elif move == "west" or move == "w":
    return 'west'
  else:
    return 'help'
  
def changeLocation(location, move):
  if location == 'the kitchen' and move == 'west':
    return 'the masterBedroom'
  elif location == 'the kitchen' and move == 'south':
    return 'the dining room'
  elif location == 'the masterBedroom' and move == 'east':
    return 'the kitchen'
  elif location == 'the masterBedroom' and move == 'south':
    return 'the living room'
  elif location == 'the dining room' and move == 'north':
    return 'the kitchen'
  elif location == 'the dining room' and move == 'west':
    return 'the living room'
  elif location == 'the living room' and move == 'north':
    return 'the masterBedroom'
  elif location == 'the living room' and move == 'east':
    return 'the dining room'
  elif location == 'the living room' and move == 'west':
    return 'Matt & Nick\'s room'
  elif location == 'Matt & Nick\'s room' and move == 'east':
    return 'the living room'
  elif location == 'Matt & Nick\'s room' and move == 'south':
    return 'Ryan & Jared\'s room'
  elif location == 'Ryan & Jared\'s room' and move == 'north':
    return 'Matt & Nick\'s room'
  else:
    locationMessage('not allowed')
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
  
# Lab 11
# Authors:  Robert Contreras and Julia Diliberto
# November 30, 2013

# Print game instructions
  printInstructions()
  
# Game play 
  while not finished:
    locationMessage(location)    
    move = getMove()
    if move == 'quit':
      finished = true
    elif move == 'help':
      printInstructions()
    else:
      printNow(location)
      location = changeLocation(location,move)
      printNow(location)

# Print ending message  
  finishGame(finished)