"""
File: mode.py
Prints the mode of a set of numbers in a file.
"""

file_name = input("Enter the file name: ")
with open(file_name, 'r') as f:
    words = [word.upper() for line in f for word in line.split()]
    word_count = {word: words.count(word) for word in set(words)}
    mode = max(word_count, key=word_count.get)
    print(f"The mode of the numbers in {file_name} is {mode:.2f}.")
