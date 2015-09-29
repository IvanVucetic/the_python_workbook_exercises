# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 51
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 51: Letter Grade to Grade Points

print "Insert your grade (A+, B-, C...):"
grade = raw_input("> ")

if grade == 'A+' or grade == 'A':
    points = 4.0
elif grade == 'A-':
    points = 3.7
elif grade == 'B+':
    points = 3.3
elif grade == 'B':
    points = 3
elif grade == 'B-':
    points = 2.7
elif grade == 'C+':
    points = 2.3
elif grade == 'C':
    points = 2
elif grade == 'C-':
    points = 1.7
elif grade == 'D+':
    points = 1.3
elif grade == 'D':
    points = 1
elif grade == 'F':
    points = 0
else:
    print "Not a valid grade."
    exit()


print "A grade %s is equivalent to %.1f points." % (grade, points)