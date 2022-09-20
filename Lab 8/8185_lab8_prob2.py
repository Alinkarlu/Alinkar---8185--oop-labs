"""
Class Animal is an abstract class move
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Method move is an abstract method of an abstract class animal"""
    @abstractmethod
    def move(self):
        return self.move
        

class Human(Animal):  
    def move(self):
        print("I can walk and run")
        

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

print(__doc__)
print(Animal.__doc__)
print("===Below is the output of code===")
human = Human()
human.move()
snake = Snake()
snake.move()
dog = Dog()
dog.move()



    