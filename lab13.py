	# Lab 13 - Lists 

	# Main Function
	# Loops through string to check for sections to replace with user input
	# These sections start with an interger
	# B = Body Part, N = Noun, V = Verb, M = Name 
def startMadLibs():
  storystring = "On Wednesday afternoon, after a day of much confusion, the university issued a statement that most of the 100 0B, preserved in formaldehyde in jars, that had disappeared from the basement of the Animal Resources Center had been disposed of by the universitys environmental health and safety officials in 2002, under protocols for biological waste.  Not everyone is convinced that the universitys explanation accounts for all the missing 1B. But if accurate, the statement resolves the status of a most unlikely collection of missing items, the 2B taken from mental patients in autopsies as far back as the 1950s. They were kept in heavy glass jars, each with an identification label, a diagnosis and the date of death, according to 3M, co-author of a new book, Malformed: Forgotten 4B of the Texas State Mental Hospital, with 5M, who 6V the brain collection."
  storylist = []
  skip = false
  word = ""
  for l in range(0, len(storystring)):
    if skip:
      skip = false
    
    elif storystring[l] == '9':
	   
      if storystring[l+1] == 'B':
        skip = true
        mlinput = requestString("Enter the name of a body part")
        word = word + mlinput
      elif storystring[l+1] == 'N':
        skip = true
        mlinput = requestString("Enter a plural noun") 
        word = word + mlinput      
      elif storystring[l+1] == 'V':
        skip = true
        mlinput = requestString("Enter a present tense verb")
        word = word + mlinput
      elif storystring[l+1] == 'M':
        skip = true
        mlinput = requestString("Enter a famous person's name")
        word = word + mlinput
      else:
        word = word + storystring[l]
    elif storystring[l] == ' ':
      storylist.append(word)
      word = ""
    else:
      word = word + storystring[l]
  storylist.append(word)
  mystring = listToString( storylist )
  printNow(mystring)
	  
def listToString( list ):
	  mystring = ""
	  for word in list:
	    mystring = mystring + word
	    mystring = mystring + " "
	  
	  return mystring

