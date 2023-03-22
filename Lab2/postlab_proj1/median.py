"""
File: median.py
Prints the median of a set of numbers in a file.
"""

file_name = input("Enter the name of the file containing the numbers: ")
with open(file_name, 'r') as file:
    numbers = [float(line.strip()) for line in file]

numbers.sort()
midpoint = len(numbers) // 2
if len(numbers) % 2 == 1:
    median = numbers[midpoint]
else:
    median = (numbers[midpoint] + numbers[midpoint - 1]) / 2
    print(f" The median of the numbers in {file_name} is {median:.2f}.")
