import math
def compute_surface_area_cyclindar(radius, height):
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * math.pow(radius, 2)
    return surface_area


radius = int(input("Enter radius:"))
height = int(input("Enter height:"))

if radius < 0:
    print ("Please enter a positive number for radius ")
    
elif height < 0:
    print ("Please enter a positive number for height ")
else:
    print("The surface Area of the cylinder with radius {0} and height {1} is: ".format(radius,height), compute_surface_area_cyclindar(radius,height))