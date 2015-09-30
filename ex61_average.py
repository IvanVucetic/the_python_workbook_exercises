# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 61
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 61: Average

print "Insert integer numbers to calculate their average. Insert 0 to finish."

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(raw_input("> "))
	sum = sum + number
	count += 1

if count == 0:
	print "Error! Entered zero as a first number."
else:
	print "Average is", sum / (count-1) # to exclude 0 from the count