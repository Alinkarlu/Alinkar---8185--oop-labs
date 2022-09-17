'''
Alinkar Lu
643040818-5
'''

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_circumference(self):
        return 2 * math.pi * self.radius

    @staticmethod
    def get_number(str):
        while True:
            try:
                number = float(input(str))
                return number
            except ValueError:
                print(f"Please enter a valid decimal number")


if __name__ == '__main__':
    radius = Circle.get_number("Enter radius:")
    circle = Circle(radius)
    print(f"The circle with radius {circle.radius}")
    print(
        f"has the area as {circle.compute_area():0.2f} and the circumference as {circle.compute_circumference():0.2f}")
