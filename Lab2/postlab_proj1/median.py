"""
File: median.py
Prints the median of a set of numbers in a file.
"""

def median(numbers):
    if len(numbers) == 0:
        return 0
    
    # Sort the list and print the number at its midpoint
    sorted_numbers = sorted(numbers)
    midpoint= len(sorted_numbers) // 2
    
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2
    else:
        return sorted_numbers[midpoint]
