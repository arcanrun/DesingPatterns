# Abstraction
"""
Мост — это структурный паттерн проектирования,
который разделяет один или несколько классов на две отдельные
иерархии — абстракцию и реализацию, позволяя изменять их независимо друг от друга.
"""
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def up(self, val):
        print("""\n==== Abstraction title ====
--- func up ---""")
        self.implementation.setUp(val)

    def down(self, val):
        print("""\n==== Abstraction title ====
        --- func down ---""")
        self.implementation.setDown(val)


class ExpandedAbstraction(Abstraction):
    def mul(self, val):
        print("""\n==== Ext Abstraction title ====
--- func mul ---""")
        print(self.implementation.getVal()*val)


# interface for Implementations
class Implementation:
    def setUp(self, value):
        raise NotImplementedError()

    def setDown(self, value):
        raise NotImplementedError()

    def getVal(self):
        raise NotImplementedError()


# concrate implementations
class ConcreteImplementationA(Implementation):
    def __init__(self):
        self.volume = 100

    def setUp(self, value):
        self.volume -= value
        print('impl A value up on: {}/value = {}'.format(value, self.volume))

    def setDown(self, value):
        self.volume -= value
        print('impl A value down on: {}/value = {}'.format(value, self.volume))

    def getVal(self):
        return self.volume


class ConcreteImplementationB(Implementation):
    def __init__(self):
        self.volume = 500

    def setUp(self, value):
        self.volume -= value
        print('impl B value up on: {}/value = {}'.format(value, self.volume))

    def setDown(self, value):
        self.volume -= value
        print('impl B value up on: {}/value = {}'.format(value, self.volume))

    def getVal(self):
        return self.volume


if __name__ == '__main__':
    A = ConcreteImplementationA()
    B = ConcreteImplementationB()

    abst_by_A = Abstraction(A)
    abst_by_B_ext = ExpandedAbstraction(B)

    abst_by_A.up(10)
    abst_by_B_ext.mul(9)