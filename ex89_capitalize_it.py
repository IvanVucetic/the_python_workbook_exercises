# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 89
# Date: 03.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 89: Capitalize It

def capitalize_it(string):
    # capitalize single i's
    for n in " ,;:.!?":
        string = string.replace(" i"+n, " I"+n)

    # capitalize the first letter
    if len(string) > 0:
        string = string[0].upper() + string[1:]

    # capitalize leters after ,.!?
    i = 0
    while i < len(string):
        if string[i] in ".!?":
            i += 1

            while i < len(string) and string[i] == " ":
                i += 1

            string = string[:i] + string[i].upper() + string[i+1:]

        i += 1
    
    return string


print capitalize_it("ti i ja i. i sta. sta")