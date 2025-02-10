
#parent class
class Animal:
    def speak(self):
        print('Animal is speaking')

    #child class/serve class/derive class
class Dog:
    def bark(self):
        print('Dog is barking')

class Cat(Dog):
    def meow(self):
        print('Cat is meowing')

a = Animal()

d = Dog()

c = Cat()


