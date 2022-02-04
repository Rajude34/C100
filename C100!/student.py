class Student(object):
    def __init__(self,name,age,gender,level,grades=None):
        self.name = name
        self.age=age
        self.gender=gender
        self.level=level
        self.grades=grades or {}

    def setGrade(self, course, grade):
        self.grades[course]=grade

    def getGrade(self,course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grade.values())/len(self.grades)

Sam = Student("Sam", 14, "male", 9, {"math":4.5})

print(Sam.age)
print(Sam.getGrade())