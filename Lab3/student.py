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
       return self.name == other.name

    def __lt__(self,other):
      """test for less than"""
      return self.name < other.name

    def __gt__(self,other):
      """test for greater than"""
      return self.name > other.name

        
        
def main():
  """A simple test."""
  student1 = Student("Don", 5)
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
  print("Student #1: "+student1.name)
  print("Student #2: "+student2.name)
  print()

  print("Is student 1 = student 2? " , end = '')
  print(student1.__eq__(student2))
  print()

  print("Is student 2 = student 1? ", end = '')
  print(student2.__lt__(student1))
  print()

  print("Is student 1 < student 2? ", end = '')
  print(student1.__lt__(student2))
  print()

  print("Is student 2 < student 1? ", end = '')
  print(student2.__lt__(student1))
  print()

  print("Is student 1 >= student 2? ", end = '')
  print(student1.__gt__(student2))
  print()

  print("Is student 2 >= student 1? ", end = '')
  print(student2.__gt__(student1))
  print()

if __name__ == "__main__":
    main()