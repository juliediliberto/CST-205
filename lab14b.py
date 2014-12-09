# CST 205
# Lab #14b
# Contributors:  Robert Contreras, Julia Diliberto, Matthew Bozelka
# December 6, 2014
# Stipulations:  


def removeSpecialChars(string):
  html_escape_table = {
     "&#8230;": "...",
     "&nbsp;": " "}
  for key, value in html_escape_table.iteritems():
    string = string.replace(key, value)
  return string
  
def titleSearch():
  webPagePath = 'C:\\Users\\GRAM\\Documents\\CST 205\\Lab 14\\DOCTYPE html.txt'
  page = open (webPagePath,"rt")
  pageString = page.read()  
  
# Create list to contain found titles
  titles = []
  
# Search for titles using "rel=\"bookmark\">" and "</a>" as a markers

  begindex = 0
  start = 0
  begmarker = "rel=\"bookmark\">"
  endmarker = "</a>"
  finish = len(pageString)
  while begindex != -1:
    begindex = pageString.find(begmarker, start, finish)
    if begindex != -1:
      begindex += len(begmarker)
    endindex = pageString.find("</a>",begindex, finish)
    endindex -= 1
    titles.append(pageString[begindex:endindex])
    start = endindex
     
# Remove unwanted characters and output titles
  for eachString in titles:
    eachString = removeSpecialChars(eachString)
    printNow (eachString)
