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

  
    """comparing two student objects"""
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
          return "Not Equal."    
        
def main():
  """A simple test."""
  student1 = Student("Don", 5)
  print()
  print(student1)
  for i in range(1, 6):
      student1.setScore(i, 100)
  print(student1)

  student2 = Student("Tomas", 5)
  print(student2)
  for i in range(1, 6):
      student2.setScore(i, 100)
  print(student2)
  print()

  print("="*50)

  print("\nStudent #1: "+student1.name)
  print("Student #2: "+student2.name, "\n")
  
  print("Student 1 = Student 2: ", student1.__eq__(student2), "\n")
  print("Student 2 = Student 1: ", student2.__eq__(student1), "\n")
  print("Student 1 < Student 2: ", student1.__lt__(student2), "\n")
  print("Student 2 < Student 1: ", student2.__lt__(student1), "\n")
  print("Student 1 >= Student 2: ", student1.__eg__(student2), "\n")
  print("Student 2 >= Student 1: ", student2.__eg__(student1), "\n")

if __name__ == "__main__":
    main()