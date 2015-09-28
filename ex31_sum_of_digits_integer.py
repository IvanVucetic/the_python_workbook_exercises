# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 31
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 31: Sum of the Digits in an Integer

print "Enter a four-digit integer:"
num = int(raw_input("> "))

tou = num // 1000
hun = (num - tou*1000) // 100
ten = (num - tou*1000 - hun*100) // 10
one = num - tou*1000 - hun*100 - ten*10

print "The sum of digits in the number is", tou+hun+ten+one