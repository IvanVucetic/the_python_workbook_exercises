# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 39
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 39: Sound Levels

print "Enter a level of noise in dB:"
sound = int(raw_input("> "))

if sound < 40:
    print "The noise is too small to be in a list."
elif sound == 40:
    print "The level of noise is the one of a quiet room."
elif 40 < sound < 70:
    print "The noise is between a quiet room and an alarm clock."
elif sound == 70:
    print "The level of noise is the one of an alarm clock."
elif 70 < sound < 106:
    print "The noise is between an alarm clock and a lawnmower."
elif sound == 106:
    print "The level of noise is the one of a lawnmower."
elif 106 < sound < 130:
    print "The noise is between a lawnmower and a jackhammer."
elif sound == 130:
    print "The level of noise is the one of a jackhammer."
else:
    print "The noise is too great to be on a list."


