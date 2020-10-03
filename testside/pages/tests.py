from django.test import TestCase

# Create your tests here.
# Exercise 1
words = "hello world"
listOfCharacters = list

"""index starts with 0 / words -2 the right ending"""
for index in range(0, len(words) - 2):
        """The 3 Characters will be written in the variable listOfCharacters"""
        listOfCharacters = words[index:index + 3]
        print(listOfCharacters)
