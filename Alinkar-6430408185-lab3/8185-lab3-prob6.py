'''
Alinkar Lu
643040818-5
'''
import functools
x = int(input("Enter an integer:"))
list = []
list2 = []  
for i in range (1,x+1):
    list.append(i**2)
    list2.append(i)
print("the sum of the square of" ,list2, "is",functools.reduce(lambda a, b: a + b, list))

    


 
