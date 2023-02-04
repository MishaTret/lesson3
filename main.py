class Human:
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f'Names of {self.brand} passengers:')
            print(self.passengers)
        else:
            print(f'There are no passengers in {self.brand}')
nick = Human(name='Nick')
kate = Human(name='Kate')
car = Auto(brand='Ford')
car.print_passengers_names()
car.add_passenger(nick)
car.print_passengers_names()
car.add_passenger(kate)
car.print_passengers_names()