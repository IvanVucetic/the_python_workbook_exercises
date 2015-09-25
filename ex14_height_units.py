# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 14
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 14: Height Units

print "Insert your height in feet and inches: "
ft = int(raw_input("feet: "))
inch = int(raw_input("inches: "))

inch += ft * 12
cm = round(inch * 2.54, 1)

print "Your height is %dcm." % cm

