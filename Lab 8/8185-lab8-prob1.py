'''
Alinkar Lu
643040818-5
'''

from abc import ABC, abstractmethod


class Animal(ABC):
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

human = Human()
human.move()
snake = Snake()
snake.move()
dog = Dog()
dog.move()


    