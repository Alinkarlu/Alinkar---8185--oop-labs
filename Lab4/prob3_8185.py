'''
Alinkar Lu
643040818-5
'''

def get_float(arg):
    correct_input = False
    while not correct_input:  # this is a while loop
        try:
            num = float(input(f"{arg}"))
            if num < 0:
                print("You can only enter a non-negative integer")
                continue
        except ValueError:
            print("Please enter a vaild integer")
        else:
            return num 
        finally:
            print("Stay healthy!")
            
   
        

if __name__ == "__main__":
    yest_case = get_float("Enter the number of new infected Covid19 cases for yesterday:")
    today_case = get_float("Enter the number of new infected Covid19 cases for today:")
    diff = 100*((today_case - yest_case)/yest_case)
    diff_float = "{:.2f}".format(diff)
    print(f"the difference of the number of new infected case is {diff_float}%")

    