def time_calculator(startTime, afterTime, weekDay):
  if (checkEmpty(startTime)):
    return "ERROR"  #Check handle errors
  elif (checkEmpty(afterTime)):
    return "ERROR"  #Check handle errors

  return add_time(startTime, afterTime, weekDay)


def checkEmpty(string):
  return string == None or len(string.strip()) == 0


def add_time(startTime, afterTime, weekDay):

  #Split String
  start = startTime.split(":")
  end = afterTime.split(":")
  minutesSplit = start[1].split(" ")  # "XX PM" --> "[XX, PM]"

  #Get minutes
  minutesEnd = int(end[1])
  minutesStart = int(minutesSplit[0])
  #Process Minute
  minutes = minutesStart + minutesEnd
  oneHour = 0
  if (minutes >= 60):
    minutes = minutes % 60
    oneHour = 1

  #Get hours
  hoursStart = int(start[0])
  hoursEnd = int(end[0])
  hoursTotal = hoursStart + hoursEnd + oneHour

  #Process hours and TimeZone
  hoursResult = hoursTotal % 24
  changeTZ = 0
  if(hoursResult == 12):
    changeTZ = 1
    hoursResult = 12
  elif (hoursResult >= 12):
    hoursResult = hoursResult - 12
    changeTZ = 1

  #Get PM/AM
  timeZoneStart = getTimeZone(minutesSplit[1], changeTZ)

  #Build strings
  strMinutes = str(minutes).zfill(2)  ## Final String Minutes
  strHours = str(hoursResult)  ## Final String Hourse
  strData = strHours + ":" + strMinutes + " " + timeZoneStart


  oneDay = 1 if isNextDay(minutesSplit[1], changeTZ) else 0
  if (checkEmpty(weekDay) and oneDay == 0):
    return strData

  #Build next day
  daysAfter = hoursTotal // 24
  daysAfter = daysAfter + oneDay
  strDays = "(next day)" if daysAfter == 1 else "(" + str(
    daysAfter) + " days later)"

  if (checkEmpty(weekDay)):
    return strData + " " + strDays

  dayResult = (switch_semana[weekDay.lower().capitalize()] + daysAfter) % 7
  for i, j in switch_semana.items():
    if j == dayResult:
      dayResult = i
      break

  if(daysAfter == 0):
    return strData + ", " + dayResult
  else:
    return strData + ", " + dayResult + " " + strDays
  
def getTimeZone(data, change):
  if (data == "AM" and change == 1):
    data = "PM"
  elif isNextDay(data, change):
    data = "AM"
  return data


def isNextDay(data, change):
  return data == "PM" and change == 1


switch_semana = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }
