"""
Alinkar Lu
643040818-5
"""
sum = 0
count = 0
end_input = False
while not end_input:
    try:
        n = float(input("Enter an integer:"))
        if n < 0:
            break
        sum = sum + n
        count = count + 1
        avg = sum / count
    except ValueError:
        print("Please enter a valid integer")
print(f"Average is {avg} ")

