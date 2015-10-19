# Ben Stephenson - The Python Workbook
#
# Exercise no. 150
# Date: 19.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 150: Remove Comments

try:
	infile = open(raw_input("input file: "), 'r')
except:
	print "A problem while opening file."
	exit()

outfile = open(raw_input("save new code to: "), 'w')

# infile.readlines() read lines into list, but just 'in infile' reads strings
for line in infile:
	# find position of # in a string. if none, position = -1
	pos = line.find("#")
	if pos > -1:
		line = line[0:pos] + "\n"
	outfile.write(line)	


infile.close()
outfile.close()


# before looking at the solution, I've created my own solution
# author's solution, that I've picked as final, is much shorter 
# and more elegant

# another difference: my solution completely removes comments, so if a line
# is entirely a comment, it will be removed using my solution, whereas it 
# is changed into a blank line in authors solution

# for line in infile.readlines():
# 	if line[0] == '#':
# 		comm = True
# 	else:
# 		comm = False
# 	for letter in line:
# 		if letter == '#':
# 			comm = True
# 		elif (letter == '\\') and (letter+1 == 'n'):
# 			comm == False
# 			outfile.write(letter)
# 		else:
# 			if comm == False:
# 				outfile.write(letter)
# 			else:
# 				pass