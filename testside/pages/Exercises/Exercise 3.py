# a)
words = "hello world"
listOfCharacters = []

"""index starts with 0 / words -2 the right ending"""
for index in range(0, len(words) - 2):
    """cutting the chars"""
    slicedChars = words[index:index + 3]
    """Sort Chars"""
    sortedChars = "".join(sorted(slicedChars))
    "Insert sortedChars to list"
    listOfCharacters.insert(index, sortedChars)
    """Print String"""
    # print(listOfCharacters[index])
    """Add aaa at the very beginning"""
listOfCharacters.insert(0, "aaa")
for p in listOfCharacters: print(p)

# b)
words = "hello world"
listOfCharacters = []

"""index starts with 0 / words -2 the right ending"""
for index in range(0, len(words) - 2):
    "Insert String to list"
listOfCharacters.insert(index, words[index:index + 3])
"""Sort List"""
listOfCharacters.sort()
"""Add aaa at the very beginning"""
listOfCharacters.insert(0, "aaa")
"""print the whole list"""
for p in listOfCharacters: print(p)
