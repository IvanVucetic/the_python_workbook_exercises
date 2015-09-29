# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 48
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 48: Chinese Zodiac

print "Insert a year: "
year = int(raw_input("> "))


if (year - 2000) % 12 == 0:
    animal = 'dragon'
elif (year - 2000) % 12 == 1:
    animal = 'snake'
elif (year - 2000) % 12 == 2:
    animal = 'horse'
elif (year - 2000) % 12 == 3:
    animal = 'sheep'
elif (year - 2000) % 12 == 4:
    animal = 'monkey'
elif (year - 2000) % 12 == 5:
    animal = 'rooster'
elif (year - 2000) % 12 == 6:
    animal = 'dog'
elif (year - 2000) % 12 == 7:
    animal = 'pig'
elif (year - 2000) % 12 == 8:
    animal = 'rat'
elif (year - 2000) % 12 == 9:
    animal = 'ox'
elif (year - 2000) % 12 == 10:
    animal = 'tiger'
else:
    animal = 'hare'

print animal