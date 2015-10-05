# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 90
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 90: Does a String Represent an Integer?

def is_integer(string):
    string = string.strip()

    if len(string) < 1:
        print "duzina ne valja"
    else:
        if all(string[i] in "0123456789" for i in range(len(string))):
            return True
        elif (string[0] in "+-") and \
        all(string[i] in "0123456789" for i in range(1,len(string))):
            return True
        else:
            return False

    
    return string

def main():
    print "Insert a string:"
    text = raw_input("> ")
    if is_integer(text):
        print "The string is an integer."
    else:
        print "The string is not an integer."

if __name__ == '__main__':
    main()


