class Student:

    # class attribute
    university_name = "Khon Kaen University"


    def __init__(self, name, *course_ids):
        self.name = name
        self.course_ids = course_ids

    def print(self):
        print(f'{self.name} registered courses {self.course_ids}')

    @classmethod
    def get_university_name(cls):
        return cls.university_name

    @classmethod
    def set_university_name(cls, university_name):
        cls.university_name = university_name


if __name__ == '__main__':
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    Student.set_university_name("KKU")
    print(f'These students are in {Student.get_university_name()}')