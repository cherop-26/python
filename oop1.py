class Student:
    def __init__(self, name,gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def study(self):
        print(self.name,"is studying")


student1 = Student("Innocent","Male",24)
print(student1.name,student1.gender,student1.age)

student2 = Student("Abigail","female",22)
print(student2.name,student2.gender,student2.age)

student3 = Student("Jim","male",22)
print(student3.name,student3.gender,student3.age)

student4 = Student("Jim","male",22)
print(student4.name,student4.gender,student4.age)