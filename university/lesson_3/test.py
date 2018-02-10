# while True:
#     a = input('input symb: ')
#     if len(a) < 10:break
# assert len(a) < 10
# print(a)



class PulseEmployee:
    titlE = "Infopulse Employee"

    def __init__(self, salery = 0, name = " ", surname = " ", position = None):
        self.name = name.title()
        self.surname = surname.title()
        self.position = position
        self.salery = salery

    def set_name(self, name):
        self.name = name


    def full_name(self):
        return self.name + " " + self.surname


    def income(self, months):
        return self.salery*months

    def increase(self, addition):
        self.salery += addition


if __name__ == "__main__":

    e6 = PulseEmployee(name="rerer", salery=100)
    print(e6.income(2))

    e7 = PulseEmployee(name = "rdsdsdr", salery=200)
    e7.increase(400)
    print(e7.salery)
    # e = PulseEmployee(name="yweert", surname="rererer")
    # e.set_name("uyuyuy")
    # print(e.name, e.surname)
    #
    #
    # e1 = PulseEmployee(name="tyytytyt", surname="rererwbvbv")
    # # e1.set_name("Lklklkk")
    # print(e1.name, e1.surname)
    #
    # e2 = PulseEmployee(name="onlyName")
    # print(e2.name)
    #
    # e3 = PulseEmployee(surname = "onlySurname")
    # print(e3.surname)
    #
    # e4 = PulseEmployee(position="QA")
    # print(e4.position)
    #
    # e5 = PulseEmployee(name = "test", salery=100)
    # print(e5.salery)

