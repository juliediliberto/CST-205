# Lab 12
# Authors:  Robert Contreras and Julia Diliberto
# November 30, 2014

def printInstructions():
  printNow(
  """***Welcome to our home!***
  Imagine you are the parent of four teenaged boys.  You find yourself in the
  kitchen one Saturday morning with a desire to make pancakes for the family.
  This ideas poses several challenges.  First, the milk is not in the kitchen.
  Second, several dishes are missing from the kitchen and finally, you're not
  sure how many people spend the night last night and will eat pancakes. 
  In each room, a description of the room will be displayed.
  You can choose to move some direction by typing \"north\", \"south\",
  \"east\" or \"west\".  You may type \"pick up\" if you want to pick up
  something in a room. You may type \"count\" to add the occupants 
  of the room to your total count. Type \"help\" if you want to see the 
  instructions again. Type "quit" if you want to leave the game.  Good luck!""")

# Prints a different message depending on the location
def locationMessage(location):

# Define location messages
  KitchenMessage = """You are now in the kitchen.  You may exit through a door to the west or to the south.
  There's a cookie jar and spatula on the counter.  Come back here to make the pancakes once you have the 
  missing supplies and know how many people are home."""
  
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
  
  PantryMessage = """You are now in the secret pantry.  You can use the chocolate chips for the
  pancakes if you want. You can go back to the kitchen through the south door."""
  
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
  elif location == 'the pantry':
    printNow(PantryMessage)
  elif location == 'not allowed':
    printNow(NotAllowed)
  else:
    printNow("Direction Undefined")
    
# Changes milkPickedUp or dishesPickedUp if appropriate
def updatePickedUp(location):
  if location == "the dining room":
    milkPickedUp == true
    printNow ("You have the milk now.")
  elif location == "Matt & Nick's room":
    dishesPickedUp == true
    printNow ("You have the dishes not.")
  else:
    printNow ("There's nothing you need for pancakes in here.")
    
# Updates the count of people in the house
def updateCount(location, count):
  if location == 'the living room':
    count = count + 3
    printNow ("That's " + str(count) + " so far")
  elif location == 'Ryan & Jared\'s room':
    count = count + 1
    printNow ("That's " + str(count) + " so far")
  elif location == 'Matt & Nick\'s room':
    count = count + 2
    printNow ("That's " + str(count) + " so far")
  else:
    printNow ("There's nobody in here to count")
  return count
# Requests, validates and stores user input regarding next move
# Possiblemoves = ['north','south','east','west','help','quit']
def getMove():
  move = requestString("What direction would you like to go in?\nType help for instructions of quit to exit the game.")
  if move == "help":
    return 'help'
  elif move == "quit":
    return 'quit'
  elif move == "pick up":
    return 'pick up'
  elif move == "count":
    return 'count'
  elif move == "north" or move == "n":
    return 'north'
  elif move == "south" or move == "s":
    return 'south'
  elif move == "east" or move == "e":
    return 'east'
  elif move == "west" or move == "w":
    return 'west'
  elif move == 'open' or move == 'o':
    return 'open'
  else:
    return 'help'
  
def changeLocation(location, move, key):
  if location == 'the kitchen' and move == 'west':
    return 'the masterBedroom'
  elif location == 'the kitchen' and move == 'south':
    return 'the dining room'
  elif location == 'the kitchen' and move == 'north' and key:
    return 'the pantry'
  elif location == 'the kitchen' and move == 'north' and not key:
    printNow("You need a key for that door.")
    return 'the kitchen'
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
  elif location == 'the pantry' and move == 'south':
    return 'the kitchen'
  else:
    locationMessage('not allowed')
    return location
# Prints ending message
def finishGame(finished):

# Define ending messages
  QuitMessage = "Tough job, huh? Thanks for trying."
  WinMessage = "You did it! Now you can make pancakes, unless it's time to take Jared to basketball practice."
  if finished:
    printNow(QuitMessage)
  else:
    printNow(WinMessage)

def playGame():
# Initialize location, finished, count, dishesPickedUp and milkPickedUp variables
  location = "the kitchen"
  finished = false
  count = 1
  dishesPickedUp = false
  milkPickedUp = false
  key = false
  
# Print game instructions
  printInstructions()
  
# Game play 
  while not (finished) and  not (location == "the kitchen" and count == 7 and dishesPickedUp and milkPickedUp):
    locationMessage(location)    
    move = getMove()
    if move == 'quit':
      finished = true
    elif move == 'help':
      printInstructions()
    elif move == 'count':
      count = updateCount(location, count)
    elif move == 'pick up':
      if location == 'the dining room':
        milkPickedUp = true
        printNow ("You've got the milk now!")
      elif location == 'Matt & Nick\'s room':
        dishesPickedUp = true
        printNow ("Great! You'll need those dishes.")
      else:
        printNow ("There's nothing you need for pancakes in here.")
    elif move == 'open' and location == "the kitchen":
      printNow ("Great job!  You opened the cookie jar and found the key to the secret pantry!\n  You can now open the door to the north if you like.")
      key = true
    else:
      location = changeLocation(location,move, key)

# Print ending message  
  finishGame(finished)
