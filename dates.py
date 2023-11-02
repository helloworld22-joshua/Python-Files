import datetime

currentDate = datetime.datetime.now()

print("Current year:", currentDate.year)
print("Current weekday:", currentDate.strftime("%A"))           # Fomats date into readable strings

myBirthDay = datetime.datetime(2006, 9, 24)                     # Set specific dates

print("My birthday:", myBirthDay.strftime("%B %d"))             # Multiple formats