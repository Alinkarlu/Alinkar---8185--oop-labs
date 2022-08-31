'''
Alinkar Lu
643040818-5
'''

class Teacher:


    def __init__(self, name, office, research, * courses):
        self.name = name
        self.office = office
        self.research = research
        self.courses = courses
        
    def office_no(self):
        return "{} has the office at {}".format(self.name, self.office)

    def research_work(self):
        return "{} is doing research in these topics {}".format(self.name,self.research)
        
    def courses_work(self):
        return "{} teaches courses {}".format(self.name, self.courses)


if __name__ == "__main__":
    manee = Teacher("Manee", "Rm.4203", "Artificial Intelligene", "EN842004", "EN13701")
    mana = Teacher("Mana", "Rm.4209", "Internet of Things", "EN842005", "EN13703")
    print(manee.office_no())
    print(manee.research_work())
    print(manee.courses_work())
    print(mana.office_no())
    print(mana.research_work())
    print(mana.courses_work())