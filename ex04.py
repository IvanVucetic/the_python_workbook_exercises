# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 4
# Date: 23.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 4: Area of a Field

print "Tell me the length of a field in feet."
length = float(raw_input("> "))
print "Tell me the width of the field in feet."
width= float(raw_input("> "))

area = (length * width) / 43.560
print "The area of the field is %s acres." % round(area,1)
