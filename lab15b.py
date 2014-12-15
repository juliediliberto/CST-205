import calendar

def birthmonth():
# Takes user input for birth date information and prints the calendar of that month
  birthYear = raw_input("Enter the year of your birth:  ")
  birthMonth = raw_input("Enter the month of your birth as an integer:  ")
  try:
    calendar.prmonth(int(birthYear),int(birthMonth))
  except ValueError: 
    showInformation("Enter appropriate integers only.  Try again")
    birthmonth()
   
def daysTilBirthday():
# Calculates and output the number of days until the user's next birthday
  currentDay = raw_input ("Enter the current day as an integer:  ")
  currentMonth = raw_input("Enter the current month as an integer:  ")
  currentYear = raw_input("Enter the current year as an integer:  ")
  birthDay = raw_input("Enter the day of your birth as an integer:  ")
  birthMonth = raw_input("Enter the month of your birth as an integer:  ")
  try:
    currentDay = int(currentDay)
    currentMonth = int(currentMonth)
    currentYear = int(currentYear)
    birthDay = int(birthDay)
    birthMonth = int(birthMonth)
  except ValueError: 
    showInformation("Enter appropriate integers only.  Try again")  
  daysTilBirthday = 0  
  if currentMonth == birthMonth:
    daysTilBirthday = int(birthDay) - int(currentDay)
  elif currentMonth < birthMonth:
    for days in range (currentDay, calendar.monthrange(currentYear,currentMonth)[1]): # add the days left in this month
      daysTilBirthday += 1
    for month in range (currentMonth + 1, birthMonth): # add the days until birthMonth
      daysTilBirthday += calendar.monthrange(currentYear,month)[1]
    for days in range (1,birthDay): #add the days in the birthMonth before birthDay
      daysTilBirthday += 1
  else:
    for days in range (currentDay, calendar.monthrange(currentYear,currentMonth)[1] + 1): # add the days left in this month
      daysTilBirthday += 1
    for month in range (currentMonth + 1, birthMonth): # add the days until birthMonth
      daysTilBirthday += calendar.monthrange(currentYear,month)[1]
    for days in range (1,birthDay): #add the days in the birthMonth
      daysTilBirthday += 1
    for month in range (1,birthMonth): #add the days in the next year until birthMonth
      daysTilBirthday += calendar.monthrange(currentYear + 1,month)[1]
    for days in range (1,birthDay):
      daysTilBirthday += 1
  showInformation ("There are " + str(daysTilBirthday) + " until your birthday.")
    
def weekdayOfDec():
  decDay = calendar.weekday(1776,7,4)
  if decDay == 0:
    showInformation ("The Declaration of Independence was signed on a Monday")
  elif decDay == 1:
    showInformation ("The Declaration of Independence was signed on a Tuesday")
  elif decDay == 2:
    showInformation ("The Declaration of Independence was signed on a Wednesday")
  elif decDay == 3:
    showInformation ("The Declaration of Independence was signed on a Thursday")
  elif decDay == 4:
    showInformation ("The Declaration of Independence was signed on a Friday")
  elif decDay == 5:
    showInformation ("The Declaration of Independence was signed on a Saturday")
  elif decDay == 6:
    showInformation ("The Declaration of Independence was signed on a Sunday")
  print decDay
  
  