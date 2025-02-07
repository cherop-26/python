# built in functons/standard -library functions

y = max(45,89,75,92,82,90,96,78)
print("The maximum value is",y)

x = min(45,26,78,69,45)
print("The minimum value is",x)

# user-defined functions
def school():
    print("Emobilis")

school()

def add():
    num1 = 5
    num2 = 7
    print(num1+num2)

add()
#Parameter/variable and Argument/Value
def multiply(a,b):
    print(a*b)

multiply(3,5)
multiply(30,7)

def employee(name,age,gender,salary,position):
    print(name,age,gender,salary,position)

employee("maureen",25,"Female","600000","CEO")
employee("John",35,"male","500000","Product manager")
employee("Gina",23,"Female","400000","Engineer")

# A program to display details of five patients in a hospital
#Using a user-defined function,implement parameter
# and argument
# fullname, gender, age, disease

def patient(fullname, gender, age, disease):
    print(fullname,gender,age,disease)

patient("Briannah","Female",23,"Pneumonia")
patient("Alex","Male",35,"Cancer")
patient("Eloise","Female",21,"Flu")
patient("George","Male",46,"Diabetes")
patient("Jake","Male",20,"Gastritis")



