# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 74
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 74: Multiplication Table

# next 4 lines- making a header
print "   ", 
for i in range(1, 11):
	print "%3i" % i,
print ""	# to make a break (new line)

for i in range(1, 11):
	for j in range(11):
		if j == 0:
			print "%3i" % i,
		elif j < 10:
			print "%3i" % (i*j), # formatting to align numbers
		else:
			print "%3i" % (i*j)	# new line after 10 (no ",")