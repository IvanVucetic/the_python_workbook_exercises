# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 55
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 55: Frequency to Name

from math import pow

print "Enter a radiation frequency in Hz:"
frequency = float(raw_input("> "))

if frequency < (3 * pow(10,9)):
	name = 'radio waves'
elif (3 * pow(10,9)) <= frequency < (3 * pow(10,12)):
	name = 'microwaves'
elif (3 * pow(10,12)) <= frequency < (4.3 * pow(10,14)):
	name = 'infrared light'
elif (4.3 * pow(10,14)) <= frequency < (7.5 * pow(10,14)):
	name = 'visible light'
elif (7.5 * pow(10,14)) <= frequency < (3 * pow(10,17)):
	name = 'ultraviolet light'
elif (3 * pow(10,17)) <= frequency < (3 * pow(10,19)):
	name = 'X-rays'
else:
	name = 'Gamma rays'

print "Electromagnetic radiation with given frequency is", name