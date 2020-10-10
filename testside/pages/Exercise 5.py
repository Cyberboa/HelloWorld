def cut_string(string):
    listOfCharacters = []
    string = input('Type in a word')
    """index starts with 0 / words -2 the right ending"""
    for index in range(0, len(string) - 2):
        "Insert String to list"
        listOfCharacters.insert(index, string[index:index + 3])
    """Sort List"""
    listOfCharacters.sort()
    return listOfCharacters


"""print the whole list"""
for p in cut_string("Hello World"): print(p)
