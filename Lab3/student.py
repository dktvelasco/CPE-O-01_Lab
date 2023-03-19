"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

  
    """equality methods"""
    def __eq__(self,other):
      """test for equality"""
      if self.name == other.name:
          return "Equal."
      else:
          return "Not Equal."

    def __lt__(self,other):
      """test for less than"""
      if self.name < other.name:
          return "Less than."
      else:
          return "Not Less than."

    def __eg__(self,other):
      """test for greater than"""
      if self.name >= other.name:
          return "Equal to or Greater than."
      else:
          return "Not Equal to or Greater than."    
    
     def shuffle(self):
        """Shuffles the student's scores in place."""
        random.shuffle(self.scores)

import random

def main():
    student1 = Student("Don ", 5)
    for i in range(1, 6):
        student1.setScore(i, 98)
    student2 = Student("Philip ", 5)
    for i in range(1, 6):
    student2.setScore(i, 87)
    student3 = Student("Protacio ", 5)
    for i in range(1, 6):
        student3.setScore(i, 95)
    student4 = Student("Rizal ", 5)
    for i in range(1, 6):
        student4.setScore(i, 85 ) 
    student5 = Student("Tomas ", 5)
    for i in range(1, 6):
        student5.setScore(i, 75)
    students = [student1, student2, student3, student4, student5]
