# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 59
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 59: Is a License Plate Valid?

print "Enter a plate number:"
plate = raw_input("> ")

validity = False

if len(plate) == 6:
    # checking just if they are upper is not enough- takes numerals as upper
    if str.isalpha(plate[0:3]) and str.isupper(plate[0:3]) and str.isdigit(plate[3:]):
        validity = True
        style = 'old'
elif len(plate) == 7:
    if str.isdigit(plate[0:4]) and str.isalpha(plate[4:]) and str.isupper(plate[4:]):
        validity = True
        style = 'new'

if validity:
    print "It's a valid plate number, %s style." % style
else:
    print "It's not a valid plate number."

#   Solutions from the book don't consider usage of str. methods.
#   Instead, each letter is checked to be A<x<Z or 0<x<9