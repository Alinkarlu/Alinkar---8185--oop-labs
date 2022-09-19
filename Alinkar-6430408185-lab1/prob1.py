correct_input = False

while not correct_input:
   try:

       temp_cel=float(input("Enter a temperature in Celsius: "))
       temp_fah = (9/5) * temp_cel + 32
       print('The %.2f degree Celsius is %.2f Fahrenheit'%(temp_cel, temp_fah)) 

   except ValueError:       
       print("Please enter a valid floating point for the temperature")
   else:
    correct_input = True

     