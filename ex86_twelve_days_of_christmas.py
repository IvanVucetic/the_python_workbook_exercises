# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 86
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 86: The Twelve Days of Christmas

def lyrics_twelve_days(n):

    from ex85_integer_to_its_ordinal_number import ordinal    

    gifts = [
    "a Partridge in a Pear Tree.",
    """Two Turtle Doves
and a Partridge in a Pear Tree.""",
    """Three French Hens,\n""",
    "4 Calling Birds,\n",
    "5 Gold Rings,\n",
    "6 Geese a-Laying,\n",
    "7 Swans a-Swimming,\n",
    "8 Maids a-Milking,\n",
    "9 Ladies Dancing,\n",
    "10 Lords a-Leaping,\n",
    "11 Pipers Piping,\n",
    "12 Drummers Drumming,\n"]

    # text for particular verse
    text = """"""
    if n > 1:
        for i in range(n-1, 0, -1):
            text = text + gifts[i]
    else:
        text = gifts[n-1]
    text += "\n"

    print """On the %s day of Christmas 
my true love sent to me""" % ordinal(n)
    print text


for i in range(1,13):
    lyrics_twelve_days(i)