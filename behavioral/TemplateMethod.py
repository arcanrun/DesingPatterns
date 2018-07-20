import abc


# abstract base class
class Person(metaclass=abc.ABCMeta):
    # tamplate method
    def do(self):
        self.inroduce()
        self.welcomeWord()
        self.hook()
        self.goodBye()

    @abc.abstractmethod
    def inroduce(self):
        pass

    @abc.abstractmethod
    def goodBye(self):
        pass

    def welcomeWord(self):
        print('Hello')

    def hook(self):
        pass

# concrete Classes
class Human(Person):
    def __init__(self, name):
        self.name = name

    def inroduce(self):
        print(self.name)

    def goodBye(self):
        print('The {} is saying: "see you later"'.format(self.name))


class Orc(Person):
    def __init__(self, name):
        self.name = name

    def inroduce(self):
        print(self.name)

    def goodBye(self):
        print('Loctar Ugar, said {}'.format(self.name))

    def hook(self):
        print('{} has 88 lvl'.format(self.name))



# clinet
def app(person):
    person.do()

if __name__ == '__main__':
    print('Human')
    print()
    app(Human('Artes'))

    print()
    print('Orc')
    print()
    app(Orc('Orc'))
