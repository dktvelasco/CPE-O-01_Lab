"""
File: stats.py
Prints the mean, median, mode of a set of numbers in a file.
"""
from mean import mean
from median import median
from mode import mode

# Simple Test Run
def main():
    print("\n===== M E 2 M O   F I N D E R ! =====")
    fileName = input("\nEnter the file name: ")
    with open(fileName, 'r')as f:
        # Input the text, convert it to numbers, and
        # add the numbers to a list
        for line in f:
            numbers = [float(line.strip())for line in f]
        numbers = []
    with open('numbers.txt') as f:
        for line in f:
            numbers.append(int(line.strip()))
    
    print("\nNumbers: ", numbers, "\n")
    print("Mean: ", f'{mean(numbers):.2f}')
    print("Median: ", f'{median(numbers):.2f}')
    print("Mode: ", f'{mode(numbers):.2f}', "\n")
    print("===== program terminated =====\n")

# The entry point for program execution
if __name__ == '__main__':
    main()
