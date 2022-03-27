"""
Author: John Cedrick A. Montilla
File: student.py
Project Description: Resources to manage a student's name and test scores.
"""

class Students(object):

    def __init__(self, name, number):
        self.name = name
        self.grade = []
        for count in range(number):
            self.grade.append(0)

    def getName(self):
        return self.name
    def setScore(self, i, score):
        self.grade[i - 1] = score
    def getScore(self, i):
        return self.grade[i - 1]
    def getAverage(self):
        return sum(self.grade) / len(self._grade)
    def getHighScore(self):
        return max(self.grade)
    def __eq__(self,student):
        if self.name == student.name:
            return "Equal"
        return "Not equal"
    def __lt__(self,student):
        if self.name < student.name:
            return "Less than"
        else:
            return "Not less than"
    def __ge__(self,student):
        if self.name >student.name:
            return "Greater than"
        elif self.name == student.name:
            return "Both are equal"
        else:
            return "Not greater or equal"

    def __str__(self):
        return "Student Name: " + self.name  + "\nResult: " + \
        " ".join(map(str, self.grade))

def main():
    student = Students("Ronald", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
        print(student)

    print(" ")
    student2= Students("Ayan",5)
    print(student2)
    for i in range(1, 6):
        student2.setScore(i, 100)
        print(student2)

    print('\nStudent 1 equal to Student 2?')
    print(student == student2)
    print('\Student 1 greater than Student 2?')
    print(student>=student2)
    print('\Student 1 less than Student 2?')
    print(student<student2)


if __name__ == "__main__":
    main()




