# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 65
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 65: Compute the Perimeter of a Polygon

from math import sqrt

print "Enter the X coordinate:"
x = float(raw_input("> "))
x_coord = [x]

print "Enter the Y coordinate:"
y = float(raw_input("> "))
y_coord = [y]

perimeter = 0

while x != "":
    print "Enter the X coordinate (blank to end):"
    try:
        x = float(raw_input("> "))
    except ValueError:
        break #PAZNJA kad se izadje iz petlje treba zatvoriti poligon
    x_coord.append(x)
    print "Enter the Y coordinate:"
    y = float(raw_input("> "))
    y_coord.append(y)

    d_x = x_coord[-1] - x_coord[-2]
    d_y = y_coord[-1] - y_coord[-2]

    side = sqrt(d_x**2 + d_y**2)
    perimeter += side

# print "Unclosed:", perimeter

# now we need to 'close' the perimeter (connect the first and the last point)
d_x = x_coord[0] - x_coord[-1]
d_y = y_coord[0] - y_coord[-1]
side = sqrt(d_x**2 + d_y**2)
perimeter += side

print "Perimeter: %.3f" % perimeter
    