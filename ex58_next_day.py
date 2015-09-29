# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 58
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 58: Next Day

print "Enter a year:"
year = int(raw_input("> "))

if (year % 400 == 0):
    leap = True
elif (year % 100 == 0):
    leap = False
elif (year % 4 == 0):
    leap = True
else:
    leap = False

print "Enter a month (number):"
month = int(raw_input("> "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

print "Enter a day:"
day = int(raw_input("> "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print "The next date is %04d-%02d-%02d." % (year, month, day)

