"""
File: mean.py
Prints the mean of a set of numbers in a file.
"""

file_name = input("Enter the name of the file containing the numbers: ")
with open(file_name, 'r')as file:
    numbers = [float(line.strip())for line in file]
    if len(numbers) == 0:
        mean = 0
    else:
        mean = sum(numbers) / len(numbers)
        print (f"The mean of the numbers in {file_name} is {mean:.2f}.")
