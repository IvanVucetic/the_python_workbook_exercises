# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 15
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 15: Distance Units

print "Insert the distance in feet:"
dist_ft = int(raw_input("> "))

miles = dist_ft / 5280.0
yards = dist_ft / 3.0
inches = dist_ft * 12

print "The distance in miles is %.2f miles." % miles
print "The distance in yards is %.2f yards." % yards
print "The distance in inches is %i inches." % inches
