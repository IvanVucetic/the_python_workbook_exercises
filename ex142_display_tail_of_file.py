# Ben Stephenson - The Python Workbook
#
# Exercise no. 142
# Date: 15.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 142: Display the Tail of a File

from sys import argv

if len(argv) < 2:
	print "No argument given."
	quit() # the same as exit() both exist for user friendliness purposes

try:
	# another way: instead of assigning argv to var and then opening it,
	# we can directly take second param from argv (which is list) and use it
	txt = open(argv[1], 'r')
except IOError:
	print "File doesn't exist."
	exit()

num_lines = sum(1 for line in txt)
print num_lines

# we need to read it for a second time
txt = open(argv[1], 'r')

for n, line in enumerate(txt):
	if n >= num_lines-10:
		print line,

# Solution that requires reading file only once (given by the book author)
# # number of lines we need
# num_lines = 10
# lines = []
# # we go through the file line by line
# for line in txt:
# 	lines.append(line)
# # once we have 10, we start poping the oldest lines, so eventually we're left with the last 10
# 	if len(lines)>num_lines:
# 		lines.pop(0)
#
# # finally, we just print from 'lines'