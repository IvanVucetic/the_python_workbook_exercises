# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 57
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 57: Is it a Leap Year?

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

print "leap year" if leap else "not a leap year"