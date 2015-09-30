# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 68
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 68: Parity Bits

data = True

while True:
	print "Enter 8 bits of data (Enter to quit):"
	data = raw_input("> ")
	if data == "":
		print "Bye!"
		exit()
	elif (len(data) != 8) or (data.count('0') + data.count('1') != 8):
		print "Not a valid 8 bit data"
		exit()
	elif data.count('1') % 2 == 0:
		print 0
	else: 
		print 1