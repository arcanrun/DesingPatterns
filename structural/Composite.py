import abc
'''
товар, коробка
product, box
'''


# interface component
class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def name(self):
        pass

    def add(self, v):
        pass

    def remove(self, v):
        pass

    def isComposite(self):
        return False


# leaf
class Product(Component):
    def __init__(self, name, price):
        self.__name = name
        self.__price = int(price)

    def name(self):
        return self.__name


# composite
class Box(Component):
    def __init__(self):
        self.__childs = []

    def name(self):
        result = []
        total_price = 0
        for i in self.__childs:
            result.append(i.name())
            # total_price += (i.price())
        return result

    def add(self, child):
        self.__childs.append(child)

    def remove(self, child):
        self.__childs.remove(child)

    def isComposite(self):
        return True




if __name__ == '__main__':
    phone_1 = Product('Samsung',1300)
    phone_2 = Product('iPhone', 900)


    print(phone_1.name())

    box_1 = Box()
    box_1.add(phone_1)
    box_1.add(phone_2)

    print('Phone box:',box_1.name())

    box_2 = Box()
    tv_1 = Product('LG', 20000)
    tv_2 = Product('Sony', 3000)

    box_2.add(tv_1)
    box_2.add(tv_2)

    print('Tv box:', box_2.name())

    big_box = Box()
    big_box.add(box_1)
    big_box.add(box_2)

    print('Big box', big_box.name())
