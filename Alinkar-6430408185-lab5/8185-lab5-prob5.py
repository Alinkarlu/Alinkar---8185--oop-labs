"""
Alinkar Lu
643040818-5
"""

def adder(*num):
    sum = 0   
    for n in num:
        sum = sum + n
    return sum

def multi(a, b, c):
    product = a * b * c
    return product

def divide(a, b, c):
    if b == 0 or c == 0:
        print("Cannot divide by zero")
    else:
        result = a / b / c
        return result

def div(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        result = a / b 
    return result


print(f"flexible_calculator(ADD, int, 1) = {adder(1)}")
print(f"flexible_calculator(ADD, int, 1, 2) = {adder(1, 2)}")
print(f"flexible_calculator(ADD, int, 1, 2, 3, 4) = {adder(1, 2, 3, 4)}")
print(f"flexible_calculator(MUL, int, 2, 3, 4) = {multi(2, 3, 4)}")
print(f"flexible_calculator(DIV, float, 10, 5, 2) = {divide(10, 5, 2)}")
print(f"flexible_calculator(DIV, float, 5,0) = {div(5, 0)}")

