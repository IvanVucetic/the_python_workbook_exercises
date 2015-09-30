# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 66
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 66: Compute a Grade Point Average

grade = "z"
sum_ = 0
count = 0

while grade != "":
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

	sum_ += points
	count += 1
	print sum_, count

# loop still adds last 'points' and 1 count when we enter ""
# that's why we need to take it away when calculating average
print "Your average grade score is %.1f" % ((sum_ - points) / (count - 1))