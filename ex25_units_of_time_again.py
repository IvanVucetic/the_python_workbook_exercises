# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 25
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 25: Units of Time (Again)

print "Enter the time period in seconds:"

time = float(raw_input("> "))

d = time // (24 * 3600)
time = time % (24 * 3600)

h = time // 3600
time %= 3600

m = time // 60
time %= 60

s = time

print "%d:%02d:%02d:%02d" % (d, h, m, s)
