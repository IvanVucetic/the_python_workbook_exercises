# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 13
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 13: Making Change

print "What is the change to be given back (e.g. $1.25, $3.47...)"
change = float(raw_input("> "))

toonies = int(change // 2)
change -= toonies * 2

loonies = int(change // 1)
change -= loonies

quarters = int(change // 0.25)
change -= quarters * 0.25

dimes = int(change // 0.1)
change -= dimes * 0.1

nickels = int(change // 0.05)
change -= nickels * 0.05

# for some reason it returns int(2.0) as 1; had to add some...
pennies = int((change / 0.01) + 0.00001) 


print "toonies: ", toonies
print "loonies: ", loonies
print "quarters: ", quarters
print "dimes: ", dimes
print "nickels: ", nickels
print "pennies: ", pennies