from inspect import CORO_SUSPENDED


class ComEnStudent:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        print(f"{self.name} has taken these courses {self.course}")

    

    
    

class CoEStudent(ComEnStudent):

    def take_courses(self,course):
        self.course = course
        super(ComEnStudent, self).__init__(course)

    

class DMEStudent(ComEnStudent):
    pass







if __name__ == "__main__":
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN13702", "EN11301", "EN11302")
    mana.take_courses("EN42005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("SC401206")
        print(com_student)