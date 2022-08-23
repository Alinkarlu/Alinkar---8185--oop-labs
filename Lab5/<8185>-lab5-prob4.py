'''
Alinkar Lu
643040818-5
'''
#def add():
#    result = num1 + num2
#    print(f"The result of adding {num1} + {num2} = {result}")

#def reduce():
#    result = num1 - num2
#    print(f"The result of reducing {num1} - {num2} = {result}")

#def multiply():
#    result = num1 * num2
#    print(f"The result of multiplying {num1} * {num2} = {result}")

#def divide():
#    if num2 == 0:
#        print("cannot divide by zero")
#    else:
#        result = num1 / num2
#        print(f"The result of dividing {num1} / {num2} = {result}")

def get_float(arg):
    correct_input = False
    while not correct_input:
        num = input(f"Please enter {arg} operand('q' to quit):")
        try:
            num = float(num)
        except ValueError:
            if num == 'q' or num == 'Q':
                exit()
            else:
                print("Please enter a valid decimal number")  
        else:
            return num 
def get_format():
    requested_format = input("Enter output format(float, int): ")
    if requested_format == "int":
        return format
    elif requested_format == "float":
        return format

def get_operator():
    #global operator
    operator = input("Please enter an operator(+,-,*,/): ")
    global result
    if operator == "+":
        
        result = num1 + num2
        return operator
    elif operator == "":
        result = num1 + num2
        return operator
    elif operator == "-":
        result = num1 - num2
        return operator
    elif operator == "*":
        result = num1 * num2
        return operator
    elif operator == "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            result = num1 / num2
            return operator
            
    else:
        print("Operation must be +,-,* or /")
        pass

def robust_calculator(num1,num2,operator,requested_format):
    if requested_format == "int":
        print("{} {} {} = {}".format(num1, operator, num2, result))
    else:
       print("{:.2f} {} {:.2f} = {:.2f}".format(num1, operator, num2, result))

if __name__ == "__main__":

    while True:
        num1 = get_float("the first")
        num2 = get_float("the second")
        operator = get_operator()
        requested_format = get_format()
        if operator is not None:
            robust_calculator(num1,num2,operator,requested_format)
        else:
            pass





        
    