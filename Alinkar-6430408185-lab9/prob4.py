#Alinkar Lu
#643040818-5

import sys
try:
    operator = sys.argv[1]
    operand1 = (sys.argv[2])
    operand2 = (sys.argv[3])
    
    try:
        operand1, operand2 = float(operand1),float(operand2)

        if operator == '+':
            print(f'{operand1} {operator} {operand2} is {operand1 + operand2}')
        elif operator == '-':
            print(f'{operand1} {operator} {operand2} is {operand1 - operand2}')
        elif operator == 'x':
            print(f'{operand1} {operator} {operand2} is {operand1 * operand2}')
        elif operator == '/':
            try:
                print(f'{operand1} {operator} {operand2} is {operand1 / operand2}')
                
            except ZeroDivisionError:
                print(f'{operand1} cannot be divided by {operand2}')
    
    except ValueError:
        print("Operands are invalid.They are not numbers")  

except IndexError:
    print("Usage:python3 prob4.py <operand1> <operator> <operand2>")

