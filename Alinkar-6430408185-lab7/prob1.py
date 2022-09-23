class Rectangle:

    def __init__(self, width=3, height=4):
        self.width = 3
        self.height = 4
    
    def __str__(self):
        return "The rectangle has width as {} height as {}".format(self.width, self.height)
    
    def set_width(self, width):
       self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height


if __name__ == '__main__':
    rect1 =Rectangle(3,4)
    print(rect1)
    print(f"Width is {rect1.get_width()}")
    rect1.set_height(5)
    print(f"Height is {rect1.get_height()}")


