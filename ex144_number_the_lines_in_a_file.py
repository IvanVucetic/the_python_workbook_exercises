# Ben Stephenson - The Python Workbook
#
# Exercise no. 144
# Date: 15.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 144: Number the Lines in a File

# take names of files
from_file = raw_input("Name the file whose lines you want numerated: ")
to_file = raw_input("Save changes to: ")


infile = open(from_file, "r")
indata = infile.readlines()

outfile = open(to_file, 'w')
i = 1
for line in indata:
	outfile.write(str(i) + ". " + line)
	i += 1

infile.close()
outfile.close()