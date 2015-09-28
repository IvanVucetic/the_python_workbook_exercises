# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 41
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 41: Note To Frequency

import math

print "Insert a note to get a Frequency (e.g. B4, A1...)"
note = raw_input("> ")

key = note[0]
octave = int(note[1])

if key == "C":
    f = 261.63
elif key == "D":
    f = 293.66
elif key == "E":
    f = 329.63
elif key == "F":
    f = 349.23
elif key == "G":
    f = 392.00
elif key == "A":
    f = 440.00
elif key == "B":
    f = 493.88

f = f / math.pow(2, 4-octave)

print "The freuency of %s is %.2f." % (note, f)