# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 30
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 30: Units of Pressure

print "Enter pressure in kilopascals:"
kpa = float(raw_input("> "))

psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325

print "The pressure is %.2f psi, %.2f mmHg, or %.2f atm." % (psi, mmhg, atm)