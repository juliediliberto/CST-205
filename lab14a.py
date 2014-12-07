# CST 205
# Lab #14
# Contributors:  Robert Contreras, Julia Diliberto, Matthew Bozelka
# December 6, 2014
# Stipulations:  Original text file was altered to fix typographical errors
#                (mot/not, d/I would) and Sam-I-Am was considered three words.


def greenEggsAndHam():
  eggsPath =  'C:\\Users\\GRAM\\Documents\\CST 205\\Lab 14\\fixedeggs.txt'
  eggs = open (eggsPath,"rt")
  eggsString = eggs.read()  

# Replace carriage returns with a space
  eggsString = eggsString.replace("\n", " ")
  
# Replace dashes with a space
  eggsString = eggsString.replace("-", " ")

# Split string into a list of words
  eggsList = eggsString.split(" ")

# Delete ""
#  eggsList.remove("")

# Create a counter dictionary with words as keys and corresponding # of occurences as values
# Count number of different words in totalWords
  counter = dict()
  totalWords = 0
  for word in eggsList:
    word = word.lower()
    if word in counter:
      counter[word] += 1
    else:
      totalWords += 1
      counter[word] = 1

# Find the word that occurs most
  greatestOccurences = 0 # Count of occurrences of most used word
  for word in counter:
    if counter[word] > greatestOccurences:
      greatestOccurences = counter[word]
      mostUsedWord = word  # Stores the word most used
      
# Output the total number of different words in eggsList
  showInformation("There are " + str(totalWords) + " words in Green Eggs and Ham")

# Output most commonly used word
  showInformation(mostUsedWord + " is the most used word in Green Eggs and Ham")
  
# Output total for each word
  printNow(counter)
