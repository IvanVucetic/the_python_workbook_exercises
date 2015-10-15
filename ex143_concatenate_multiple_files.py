# Ben Stephenson - The Python Workbook
#
# Exercise no. 143
# Date: 15.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 143: Concatenate Multiple Files

from sys import argv

if len(argv) < 2:
	print "No parameters provided. Exiting..."
	exit()

indata = ""

# file by file
for i in range(1,len(argv)):
	try:
		infile = open(argv[i],'r')
		temp = infile.read()
		indata = indata + temp
	except IOError:
		print "File %s doesn't exist, proceeding to next..." % argv[i]
		pass

print "All files read, printing..."
print ""
print indata