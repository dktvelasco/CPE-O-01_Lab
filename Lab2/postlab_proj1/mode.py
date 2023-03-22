"""
File: mode.py
Prints the mode of a set of numbers in a file.
"""

def mode(numbers):
    if len(numbers) == 0:
        return 0
    
    mode_count = 0
    mode_value = numbers[0]
    
    for value in numbers:
        count = numbers.count(value)
        if count > mode_count:
            mode_count = count
            mode_value = value
    
    return mode_value
    
