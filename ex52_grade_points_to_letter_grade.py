# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 52
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 52: Grade Points to Letter Grade

print "Insert your grade points:"
points = round(float(raw_input("> ")), 1)

if points >= 4.0:
	grade = 'A+'
elif 4.0 > points > 3.85:
	grade = 'A'
elif 3.85 > points > 3.5:
	grade = 'A-'
elif 3.5 > points > 3.15:
	grade = 'B+'
elif 3.15 > points > 2.85:
	grade = 'B'
elif 3.85 > points > 2.5:
	grade = 'B-'
elif 2.5 > points > 2.15:
	grade = 'C+'
elif 2.15 > points > 1.85:
	grade = 'C'
elif 1.85 > points > 1.5:
	grade = 'C-'
elif 1.5 > points > 1.15:
	grade = 'D+'
elif 1.15 > points > 1:
	grade = 'D'
else:
	grade = 'F'

print "A grade for %s points is %s." % (points, grade)