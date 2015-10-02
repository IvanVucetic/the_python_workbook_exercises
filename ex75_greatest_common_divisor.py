# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 75
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 75: Greatest Common Divisor

print "This programs calculates the greatest common divisor of 2 numbers."
print "Insert numbers:"
a = int(raw_input("a: "))
b = int(raw_input("b: "))

d = a if a < b else b

while (a % d != 0) or (b % d != 0): # smanjuje kad je bilo koji nedeljiv
	d = d - 1						# AND bi smanjivao samo kad su oba nedeljiva

print "The greatest common divisor of %s and %s is: %s" % (a, b, d)