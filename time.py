import datetime

# define the writing time
startTime = datetime.time(10, 15, 0)
endTime = datetime.time(15, 30, 0)

# function that compares the given time against start and end
def isOpen(startTime, endTime, x):
    if startTime <= endTime:
        return startTime <= x <= endTime
    else:
        return startTime <= x or x <= endTime

# Getting current time
currentTime = datetime.datetime.now().time()

# Compare to writing hours
if isOpen(startTime, endTime, currentTime):
  print('Do something')
else:
  print('Nah fam.')