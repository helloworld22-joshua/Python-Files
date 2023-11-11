import datetime

currentDate = datetime.datetime.now()

print("Current year:", currentDate.year)
print("Current weekday:", currentDate.strftime("%A"))           # Fomats date into readable strings

myBirthDay = datetime.datetime(2006, 9, 24)                     # Set specific dates

print("My birthday:", myBirthDay.strftime("%B %d"))             # Multiple formats

name = "Joshua"
money = 27
str1 = "This is {0}. {0} has {1:.2f}€ in his bank account."

print(str1.format(name, money))

str2 = "I am {age} years old and live in {country}."

print(str2.format(age = "17", country = "Germany"))