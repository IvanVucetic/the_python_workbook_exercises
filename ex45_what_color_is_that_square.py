# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 45
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 45: What Color is that Square?

print "Insert chess position (e.g. 'a4'):"
position = raw_input("> ")

col = position[0] 	# a, b, c...
row = int(position[1]) 	# 1, 2, 3...

if col in ('a', 'c', 'e', 'g'):
	starts = 'black'
else:
	starts = 'white'

print "The column starts with a %s square." % starts

if starts == 'black':
	if (row % 2 == 0):
		field = 'white'
	else:
		field = 'black'
else:
	if (row % 2 == 0):
		field = 'black'
	else:
		field = 'white'

print "The position %s is %s." % (position, field)




