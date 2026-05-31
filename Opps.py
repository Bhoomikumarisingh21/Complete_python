#class & object
class Student:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

s = Student("Bhoomi Kumari Singh")
s.display()

#Inheritence
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    pass

c = Child()
c.show()

#Encapsulation
class Student:
    def __init__(self):
        self.__marks = 90   # Private variable

    def get_marks(self):
        return self.__marks

s = Student()

print("Marks:", s.get_marks())

#Abtraction
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

#Polimorphism
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()