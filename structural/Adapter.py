import abc, math


# client interface
class Math:
    @abc.abstractmethod
    def math(self, v):
        pass


# third-party service
class LibrarySupportMath:
    # different interface dosqrt != math
    # so the Adapter do the things
    def dosqrt(self, v):
        try:
            return math.sqrt(float(v))
        except Exception:
            return 'Error'


# adapter
class Adapter(Math):
    def __init__(self, adapt):
        self.__adapt = adapt

    def math(self,v):
        return self.__adapt.dosqrt(v)

# out function
class Sqrt(Math):
    def math(self, v):
        return v**(0.5)


def client(func, v):

    print(func.math(v))

if __name__ == '__main__':
    func_1 = Sqrt()
    client(func_1, 16)

    func_2 = LibrarySupportMath()
    adapter = Adapter(func_2)

    client(adapter, 16)
