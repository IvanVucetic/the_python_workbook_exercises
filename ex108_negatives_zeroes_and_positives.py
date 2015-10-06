# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 108
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 108: Negatives, Zeros and Positives

neg = []
zer = []
pos = []

print "Enter a value (blank to finish):"
try:
	value = int(raw_input("> "))
except ValueError:
	print "Bye!"
	exit()
if value < 0:
	neg.append(value)
elif value == 0:
	zer.append(value)
else:
	pos.append(value)

while True:
	try:
		value = int(raw_input("> "))
	except ValueError:
		break
	if value < 0:
		neg.append(value)
	elif value == 0:
		zer.append(value)
	else:
		pos.append(value)

for v in neg:
	print v
for v in zer:
	print v
for v in pos:
	print v

# All this mess with try-except error could be avoided by
# using input instead of raw_input; it evaluates input itself
# so we could just say while value != ""...
