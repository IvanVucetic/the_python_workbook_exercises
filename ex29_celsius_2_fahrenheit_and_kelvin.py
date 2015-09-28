# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 29
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 29: Celsius to Fahrenheit and Kelvin

print "Enter the temperature in degrees Celsius:"
tc = float(raw_input("> "))

tk = tc + 274.15
tf = tc*(9/5) + 32

print "The temperature is %.1f Kelvin, i.e. %.1f degrees Fahrenheit" % (tk, tf)
