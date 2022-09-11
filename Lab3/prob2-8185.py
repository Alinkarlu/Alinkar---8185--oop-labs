'''
Alinkar Lu
643040818-5
'''

fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
print(f"The fruits are", (fruits))

for number, letter in enumerate(fruits, start=1):
    print(number, letter.upper())

for i in range (len(fruits)):
    fruits.sort()
    fruits[i] = fruits[i].upper()
print("After sorting fruits,fruits are" , (fruits))

#Name = Alinkar Lu
#ID = 643040818-5


