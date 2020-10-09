from django.test import TestCase


# Create your tests here.
# Exercise 1
def cut_string(string):
    listOfCharacters = []
    string = input('Type in a word')
    """index starts with 0 / words -2 the right ending"""
    for index in range(0, len(string) - 2):
        "Insert String to list"
        listOfCharacters.insert(index, string[index:index + 3])
        "Insert String to myScript.txt"
        add_to_file(string[index:index + 3])
    """Sort List"""
    listOfCharacters.sort()
    return listOfCharacters


"""Method to add string to file"""


def add_to_file(string):
    # open file with
    file = open('myScript.txt', "a")
    # write the string into thefile
    file.write("".join(string))
    # creating a new line
    file.write("\n")
    # close the file
    file.close()
    return file


print(cut_string("Hello World "))
openFile = open('myScript.txt')
readfile = openFile.read()
print(readfile)
