# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 112
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 112: Below and Above Average

values = []
print "Enter a number(blank to exit):"
val = raw_input("> ")

while val != "":
	values.append(float(val))
	print "Enter a number(blank to exit):"
	val = raw_input("> ")

avg = sum(values) / len(values)
below = []
average = []
above = []

for i in values:
	if i > avg:
		above.append(i)
	elif i < avg:
		below.append(i)
	else:
		average.append(i)

print "The average value is %.1f" % avg
print "The values below average are:", below
if len(average) > 0:
	print "There are average values:", average
print "The values above average are:", above
