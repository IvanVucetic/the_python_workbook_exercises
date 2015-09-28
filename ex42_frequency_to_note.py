# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 42
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 42: Frequency To Note

print "Insert frequency (Hz):"
freq = float(raw_input("> "))

if (260.63 <= freq <= 262.63):
	note = "C4"
elif (292.66 <= freq <= 294.66):
	note = "D4"
elif (328.63 <= freq <= 330.63):
	note = "E4"
elif (348.2 <= freq <= 350.23):
	note = "F4"
elif (391 <= freq <= 393):
	note = "G4"
elif (439 <= freq <= 441):
	note = "A4"
elif (492.88 <= freq <= 494.88):
	note = "B4"
else:
	note = "unknown"
print "The note with the frequency %.2f is %s." % (freq, note)