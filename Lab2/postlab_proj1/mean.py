"""
File: mean.py
Prints the mean of a set of numbers in a file.
"""

def mean(numbers):
    if len(numbers) == 0:
        return 0
    
    return sum(numbers) / len(numbers)
