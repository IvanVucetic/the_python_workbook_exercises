# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 117
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 117: Line of Best Fit

xcoor = []
ycoor = []

x = raw_input("Insert x (blank to stop): ")

while x != "":
	xcoor.append(float(x))
	y = float(raw_input("Insert y: "))
	ycoor.append(y)
	x = raw_input("Insert x (blank to stop): ")

x_avg = sum(xcoor) / len(xcoor)
y_avg = sum(ycoor) / len(ycoor)

sumxy = 0
for i in range(len(xcoor)):
	sumxy = sumxy + xcoor[i]*ycoor[i]

sumx2 = 0
for x in xcoor:
	sumx2 = sumx2 + x**2

m_numer = sumxy - (sum(xcoor)*sum(ycoor) / len(xcoor))
m_denom = sumx2 - (sum(xcoor)**2 / len(xcoor))
m = m_numer / m_denom

b = y_avg - m*x_avg

print "The best fit:"
print "y = %gx + %g" % (m, b)	# %g removes trailing zeroes

