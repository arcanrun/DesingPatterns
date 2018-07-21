import abc


# interface component
class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, visitor):
        pass


# concrete components
class One(Component):
    def accept(self, visitor):
        visitor.visitOne(self)

    def introOne(self):
        return 'Hello, I am One elem'


class Two(Component):
    def accept(self, visitor):
        visitor.visitTwo(self)

    def introTwo(self):
        return 'Hello, I am Two elem'


class Three(Component):
    def accept(self, visitor):
        visitor.visitThree(self)

    def introThree(self):
        return 'Hello, I am Three elem'


# interface visitor
class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visitOne(self, one: One()):
        pass

    @abc.abstractmethod
    def visitTwo(self, two :Two()):
        pass

    @abc.abstractmethod
    def visitThree(self, three: Three()):
        pass


# concrete Visitor
class Converter(Visitor):
    def visitOne(self, one):
        print(one.introOne() + '--visitor was here')

    def visitTwo(self, two):
        print(two.introTwo() + '--visitor was here')

    def visitThree(self, three):
        print(three.introThree() + '--visitor was here')


# client code
def app(components: list, vis):
    for i in  components:
        i.accept(vis)


if __name__ == '__main__':
    components = [One(), Two(), Three()]
    visitor = Converter()
    app(components, visitor)