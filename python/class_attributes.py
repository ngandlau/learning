from dataclasses import dataclass


class Employee:
    # class variables
    name: str
    company: str = 'Deutsche Bahn'

    def __init__(self, name):
        self.name = name

    def set_name(self, new_name):
        self.name = new_name


@dataclass
class EmployeeDataclass:
    # dataclass turns class variables into instance variables
    name: str
    company: str = 'Deutsche Bahn'

    def set_name(self, new_name):
        self.name = new_name


if __name__ == '__main__':
    nils = Employee('Nils')
    alex = Employee('Alex')

    print(nils.name) # Nils
    print(alex.name) # Alex
    print('-------')

    alex.name = 'Fabian'
    print(nils.name) # Nils
    print(alex.name) # Fabian
    print('-------')

    alex.set_name('Christoph')
    print(nils.name) # Nils
    print(alex.name) # Christoph
    print('-------')

    Employee.name = 'WTF'
    print(nils.name) # Nils
    print(alex.name) # Christoph
    print('-------')

    nils.name = Employee.name
    print(nils.name) # WTF
    print(alex.name) # Christoph

