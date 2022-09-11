"""
Alinkar Lu
643040818-5
"""

def factorial(n):
        if n == 1:
            return 1
        elif n > 0:
            return factorial(n-1)*n
        else:
            print("Please enter an integer that is non-negative")
            exit()

            
while True:
    try:  
        n = int(input("Enter an integer:"))
        print(f"factorial({n}) is {factorial(n)}")
        continue
    except ValueError:
        print("Please enter a valid integer")
        exit()

   
