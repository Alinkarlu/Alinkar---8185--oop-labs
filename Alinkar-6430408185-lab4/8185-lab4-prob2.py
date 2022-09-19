'''
Alinkar Lu
643040818-5
'''
def get_float(arg):
    correct_input = False
    while not correct_input:
        try:
            num = float(input(f"Please enter {arg} floating point number:"))
        except ValueError:
            print("Please enter a valid floating point number")  
        else:
            return num 

def add():
    result = num1 + num2
    print(f"The result of adding {num1} + {num2} = {result}")

def reduce():
    result = num1 - num2
    print(f"The result of reducing {num1} - {num2} = {result}")

def multiply():
    result = num1 * num2
    print(f"The result of multiplying {num1} * {num2} = {result}")

def divide():
    if num2 == 0:
        print("cannot divide by zero")
    else:
        result = num1 / num2
        print(f"The result of dividing {num1} / {num2} = {result}")
    
  

if __name__ == "__main__":
    num1 = get_float("the first")
    num2 = get_float("the second")
    operator = input("Please enter an operator(+,-,*,/): ")
    if operator == '+':
        add()
    elif operator == '-':
        reduce()
    elif operator == '*':
        multiply()
    elif operator == '/':
        divide()
    else:
        print("Unknown operator")