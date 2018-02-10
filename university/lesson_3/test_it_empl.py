from test import PulseEmployee

class ITEmplotee(PulseEmployee):
    def __init__(self, salery = 0, name = " ", surname = " ", position = None):
        PulseEmployee.__init__(self, salery, name, surname, position)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    def add_skills(self, *skills_list):
        self.skills.extend(skills_list)



e = ITEmplotee(name="Dima", salery=1000)
e.add_skill("GIT")
print(e.skills)

e.add_skills("C++", "OOP", "C#")
print(e.skills)