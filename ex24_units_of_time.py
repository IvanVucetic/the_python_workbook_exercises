# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 24
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 24: Units of Time

print "Enter the time period you want translated into seconds:"

d = int(raw_input("days> ")) * 3600 * 24
h = int(raw_input("hours> ")) * 3600
m = int(raw_input("minutes> ")) * 60
s = int(raw_input("seconds> "))

time = d + h + m + s

print "The period ammounts to %i seconds" % time