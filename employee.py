class Employee:
    def __init__(self, name,position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(self.position,"is earning",self.salary)

empolyee1 = Employee("John","CEO",750000)
print(empolyee1.name,empolyee1.position,)
print(empolyee1.info())

employee2 = Employee("Jane","Manager",350000)
print(employee2.name,employee2.position,employee2.salary)

employee3 = Employee("Gina","Director",650000)
print(employee3.name,employee3.position,employee3.salary)




