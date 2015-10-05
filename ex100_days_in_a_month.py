# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 100
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 100: Days in a Month

def days_in_month(month, year):
	# check for year leap (done in exercise 57)
	if (year % 400 == 0):
		leap = True
	elif (year % 100 == 0):
		leap = False
	elif (year % 4 == 0):
		leap = True
	else:
		leap = False

	if month in [4,6,9,11]:
		days = 30
	elif month == 2:
		days = 29 if leap else 28
	else:
		days = 31

	return days

def main():
	print "Insert a month (1-12):"
	month = int(raw_input("> "))
	print "Insert a year (YYYY):"
	year = int(raw_input("> "))

	days = days_in_month(month, year)
	print "That month has %i days." % days

main()