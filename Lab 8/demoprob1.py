from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def __str__(self):
        pass

    def get_taste(self):
        return self.get_taste

    def set_taste(self,taste):
        self.taste = taste

class Orange(Fruit):
    def __init__(self, name):
        super(Orange.self).__init__()

orange1 = Orange("Orange")
orange1.set_taste("sweet and sour")
print(orange1)
