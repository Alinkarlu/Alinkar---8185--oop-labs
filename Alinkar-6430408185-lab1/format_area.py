import math
print("radius \theight \tsurface area")

for radius in range (1,11):
    height = 2*radius
    surf_area = 2*math.pi*radius*(radius + height)
    print(f'{radius:6} {height:7} {surf_area:13.2f}')