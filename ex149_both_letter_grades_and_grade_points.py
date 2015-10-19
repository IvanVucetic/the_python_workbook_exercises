# Ben Stephenson - The Python Workbook
#
# Exercise no. 149
# Date: 19.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 149: Both Letter Grades and Grade grade

print "Insert a grade to be converted:"
grade_from = raw_input("> ")

while grade_from != "":
	try:
		grade_from = round(float(grade_from), 1)

		if grade_from >= 4.0:
			grade = 'A+'
		elif 4.0 > grade_from > 3.85:
			grade = 'A'
		elif 3.85 > grade_from > 3.5:
			grade = 'A-'
		elif 3.5 > grade_from > 3.15:
			grade = 'B+'
		elif 3.15 > grade_from > 2.85:
			grade = 'B'
		elif 3.85 > grade_from > 2.5:
			grade = 'B-'
		elif 2.5 > grade_from > 2.15:
			grade = 'C+'
		elif 2.15 > grade_from > 1.85:
			grade = 'C'
		elif 1.85 > grade_from > 1.5:
			grade = 'C-'
		elif 1.5 > grade_from > 1.15:
			grade = 'D+'
		elif 1.15 > grade_from > 1:
			grade = 'D'
		else:
			grade = 'F'

	except ValueError:

		if grade_from == 'A+' or grade_from == 'A':
		    grade = 4.0
		elif grade_from == 'A-':
		    grade = 3.7
		elif grade_from == 'B+':
		    grade = 3.3
		elif grade_from == 'B':
		    grade = 3
		elif grade_from == 'B-':
		    grade = 2.7
		elif grade_from == 'C+':
		    grade = 2.3
		elif grade_from == 'C':
		    grade = 2
		elif grade_from == 'C-':
		    grade = 1.7
		elif grade_from == 'D+':
		    grade = 1.3
		elif grade_from == 'D':
		    grade = 1
		elif grade_from == 'F':
		    grade = 0
		else:
		    grade = 'unavailable - Not a valid grade to convert from.'

	print "Converted grade is", grade 
	print "Insert a grade to be converted (blank to exit):"
	grade_from = raw_input("> ")

