import random

def getWords(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        words_tuple = tuple(words)
        return words_tuple
