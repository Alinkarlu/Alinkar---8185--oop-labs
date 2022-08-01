correct_input = False
while not correct_input:
    try:
        num1 = float(input("Please enter the first floating point number: "))
    except ValueError:
        print("Please enter a valid floating point number")
    else:
        correct_input = True
correct_input = False
while not correct_input:
    try:
        num2 = float(input("Please enter the second floating point number: "))
        result = num1 + num2
        print(f"The result of adding {num1} + {num2} = {result}")
    except ValueError:
        print("Please enter a valid floating point number")
    else:
        correct_input = True

