"""
Alinkar Lu
643040818-5
"""

class Student:

    university_name = "Khon Kaen University"

    def __init__(self, name, * course_ids):
        self.name = name
        self.course_ids = course_ids
    
    def describe(self):
        return "{} registered courses {}".format(self.name, self.course_ids) 


if __name__ == "__main__":
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842094", "842095", "813701")
    chujai = Student("Chujai", "842004", "842005")
    print(manee.describe())
    print(mana.describe())
    print(chujai.describe())
    print(f"These students are in {Student.university_name}")