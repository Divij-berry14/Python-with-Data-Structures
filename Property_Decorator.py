class Student:
    def __init__(self, grade, name):
        self.name = name
        self.grade = grade

    def msg(self):
        return self.name + " got grade " + self.grade

stud1 = Student("B", "Davij")
stud1.grade = "A"
print("Name:", stud1.name)
print("Grade:", stud1.grade)
print("Message:", stud1.msg())
