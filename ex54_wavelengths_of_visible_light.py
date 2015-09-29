# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 54
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 54: Wavelengths of Visible Light

print "Insert a wavelength in nanometers:"
wavelength = int(raw_input("> "))

if 380 <= wavelength < 450:
	color = 'violet'
elif 450 <= wavelength < 495:
	color = 'blue'
elif 495 <= wavelength < 570:
	color = 'green'
elif 570 <= wavelength < 590:
	color = 'yellow'
elif 590 <= wavelength < 620:
	color = 'orange'
elif 620 <= wavelength < 750:
	color = 'red'
else:
	color = 'outside of the visible spectrum'

print "The color with that wavelength is %s." % color