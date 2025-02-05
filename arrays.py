from collections.abc import coroutine

courses = [ "MIT","Cybersecurity","Datascience",]
print(courses)

#Accessing an element
print(courses[2])

#looping through an array
for x in courses:
    print("courses is",x)

#Adding a new element
courses.append("laravel")
print(courses)

#Removing an element
courses.remove("Cybersecurity")
print(courses)