# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 8
# Date: 24.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 8: Widgets and Gizmos

print "Number of widgets?"
w = int(raw_input("> "))
print "Number of gizmos?"
g = int(raw_input("> "))

print "The total weight of the package is %i grams" % (w * 75 + g * 112)