# CST 205
# Lab #14
# Contributors:  Robert Contreras, Julia Diliberto, Matthew Bozelka
# December 6, 2014
# Stipulations:  


def titleSearch():
  webPagePath = 'C:\\Users\\GRAM\\Documents\\CST 205\\Lab 14\\DOCTYPE html.txt'
  page = open (webPagePath,"rt")
  pageString = page.read()  
  

# Create list to contain found titles
  titles = []
  
# Search for titles using "rel=\"bookmark\">" and "</a>" as a markers

  begindex = 0
  start = 0
  finish = len(pageString)
  while begindex != -1:
    begindex = pageString.find("rel=\"bookmark\">", start, finish)
    if begindex != -1:
      begindex += 16
    endindex = pageString.find("</a>",begindex, finish)
    endindex -= 1
    titles.append(pageString[begindex:endindex])
    start = endindex
    
# Remove unwanted characters
  for i in range(0,len(titles)):
 #   index = titles[i].find("&nbsp;")
    printNow(titles[i])
    titles[i].replace("&nbsp;", " ")# = (titles[i][:index] + titles[i][index+6:])
    titles[i].replace("\x92", "\'")
    printNow(titles[i])
# Output titles
# printNow ( titles)