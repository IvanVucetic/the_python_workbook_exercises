# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 32
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 32: Sort 3 Integers

a = int(raw_input("Insert first number: "))
b = int(raw_input("Insert second number: "))
c = int(raw_input("Insert third number: "))

min_ = min(a, b, c)
max_ = max(a, b, c)
mid_ = (a + b + c) - min_ - max_

print "Numbers in sorted order:", min_, mid_, max_