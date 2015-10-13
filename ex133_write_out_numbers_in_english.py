# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 133
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 133: Write Out Numbers in English

def num2string(num):
    singles = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', \
             7: 'seven', 8:'eight', 9:'nine', 0:'zero'}

    decades = {10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',\
               60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

    if len(str(num)) == 3: #cant check len on int; other option if > 99
        output = singles[num/100] + " hundred " + decades[num%100 - num%10]\
             + " " + singles[num%10]
    elif len(str(num)) == 2:
        output = decades[num - num%10] + " " + singles[num%10]
    elif len(str(num)) == 1:
        output = singles[num]

    return output

def main():
    num = raw_input("Insert a number between 0 and 999: ")
    try:
        num = int(num)
        if 0 < num < 999:
            print num2string(num)
        else:
            print "Must be a number between 0 and 999."
    except ValueError:
        print "Not a valid number."
        exit()



main()