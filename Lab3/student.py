class Student(object):


  # constructor to initialize the object

  def __init__(self, name, number):


    self.name = name

    self.scores = []

    for count in range(number):

      self.scores.append(0)


  # method to get the name

  def getName(self):


    return self.name


  # method to set the score

  def setScore(self, i, score):


    self.scores[i - 1] = score


  # method to get the score

  def getScore(self, i):


    return self.scores[i - 1]


  # method to get the average

  def getAverage(self):


    return sum(self.scores) / len(self._scores)


  # method to get the high score

  def getHighScore(self):


      return max(self.scores)


  # method to print the object in string format

  def __str__(self):


    return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))


  # checking for equality for the names

  def __eq__(self,other):


    if self.name == other.name:

      return "Equal"

    else:

      return "Not Equal"


  # checking for less than in names

  def __lt__(self,other):


    if self.name < other.name:

      return "Less than"   

    else:

      return "Not less than"


  # checking for greater than or equal to names

  def __ge__(self,other):


    if self.name >other.name:

      return "Greater than"

    elif self.name == other.name:

      return "Both are equal"

    else:

      return "Not greater or equal"



# main function

def main():


  # creating student object

  student = Student("Ken", 5)

  print(student)

  for i in range(1, 6):

    student.setScore(i, 100)

    print(student)


  # creating student2 object

  student2= Student("Ayan",5)

  print(student2)

  for i in range(1, 6):

    student2.setScore(i, 100)

    print(student2)


  # checking the equality methods

  print("student==student2" , student==student2)

  print("student<student2",student<student2)

  print("student2<student",student2<student)

  print("student>=student2",student>=student2)



# calling the main function

if __name__ == "__main__":

  main()
