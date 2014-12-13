import random

def diceRoll():
  roll = random.randint(1,6)
  return roll

def craps():
 
  over = false
  matchset = false
  while over == false:
    roll1 = diceRoll()
    roll2 = diceRoll()
    total = roll1 + roll2
    if matchset == false:
      if total == 7 or total == 11:
        over = true
        win = true
        showInformation("You win with first roll of 7 or 11!")
      elif total == 2 or total == 3 or total == 12:
        over = true
        win = false
        showInformation("You lose with a first roll of 2, 3 or 12.")
      else:
        matchset = true
        match = total
        showInformation("Total to match is " + str(total) + ".")
    else:
      if total == 7:
        over = true
        win = false
        showInformation("You lose with a roll of 7.")
      else:
        if total == match:
          over = true
          win = true
          showInformation ("That's a match! You win!")
          