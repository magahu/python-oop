#BASIC HERITANCE EXAMPLE
class Person:
    def __init__(self, name):
        self.name = name

    def go(self):
        print('My name\'s {}. Let\'s go party!'.format(self.name))

class Cyclist(Person):
    def __init__(self, name):
        super().__init__(name)

    def go(self):
        print('My name\'s {}. Let\'s go for a ride on my bike!'.format(self.name))

class Runner(Person):
    def __init__(self, name):
        super().__init__(name)

    def go(self):
        print('My name\'s {}. Let\'s go for running!'.format(self.name))


def main():
    juan = Person('Juan')
    juan.go()

    vale = Cyclist('Valeria')
    vale.go()

    ernesto = Runner('Ernesto')
    ernesto.go()

if __name__ == '__main__':
    main
