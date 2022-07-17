correct_input = False

while not correct_input:
   try:
        
        std_id = float(input("Please enter your student ID: "))
        midterm_mark = float(input("Please enter the student's midterm exam mark(0-100): "))
        if midterm_mark < 0 or midterm_mark > 100:
            print("Please enter the score in the range [0, 100]")
            continue
            

        final_mark = float(input("Please enter the student's final exam mark(0-100): "))
        if final_mark < 0 or final_mark > 100:
            print("Please enter the score in the range [0, 100]")
            continue

        total_mark = midterm_mark*(40/100)+final_mark*(60/100)

        if total_mark >= 80:
            grade = 'A'
        elif total_mark >= 70:
            grade = 'B'
        elif total_mark >= 60:
            grade = 'C'
        elif total_mark >= 50:
            grade = 'D'
        else:
            grade = 'F'
        print('student ID %d has the total mark as %d and grade is %s' % (std_id, total_mark, grade))    


   except ValueError:       
       print("Please enter the score as a decimal number")
   else:
    correct_input = True

# Name = Alinkar Lu
# Student ID = 643040818-5