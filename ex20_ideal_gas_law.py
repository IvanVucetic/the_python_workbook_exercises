# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 20
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 20: Ideal Gas Law

print "Enter the ammount of pressure in Pascals:"
pressure = float(raw_input("> "))

print "Enter a volume of a tank in litres:"
vol = float(raw_input("> "))

print "Enter a temperature in degrees Celsius:"
temp_c = float(raw_input("> "))
temp_k = temp_c + 273.15

r_constant = 8.314 # Joules / (mol * K)

n = (pressure * vol) / (r_constant * temp_k) 

print "The amount of gas is %.2f moles." % n