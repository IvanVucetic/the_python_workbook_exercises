# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 49
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 49: Richter Scale

print "Please enter a magnitude of an earthquake:"
magn = round(float(raw_input("> ")), 1)

if magn < 2.0:
    desc = 'micro'
elif magn < 3.0:
    desc = 'very minor'
elif magn < 4.0:
    desc = 'minor'
elif magn < 5.0:
    desc = 'light'
elif magn < 6.0:
    desc = 'moderate'
elif magn < 7.0:
    desc = 'strong'
elif magn < 8.0:
    desc = 'major'
elif magn < 10.0:
    desc = 'great'
else:
    desc = 'meteoric'

print "A %s earthquake is considered to be a %s earthquake." % (magn, desc)

