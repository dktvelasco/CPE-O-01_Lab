"""
File: mean.py
Prints the mean of a set of numbers in a file.
"""

fileName = input("Enter the file name: ")
f = open(fileName, 'r')

# Input the text, convert it to numbers, and
# add the numbers to a list
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

# Sort the list and print the sum of all numbers divided by its length
numbers.sort()
mean = sum(numbers) / len(numbers)
print("\nThe mean is", end=" ",)
if len(numbers) == 0:
    print(0)
else:
    print (sum(numbers) / len(numbers))

