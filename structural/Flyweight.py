import abc

# flyweight interface
class Flyweight(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, x, y):
        pass


# concrete flyweight
class PixelColor(Flyweight):
    def __init__(self, color):
        self.__color = color

    def create(self, x, y):
        print('{} at the {} {}'.format(self.__color, x, y))


# flyweight factory
class FlyweightFactory:
    def __init__(self):
        self.__storage = {}

    def get_pixel(self, key):
        try:
            pixel = self.__storage[key]
        except KeyError:
            pixel = PixelColor(key)
            self.__storage[key] = pixel
        return pixel

    def list_pixel(self):
        for k, v in self.__storage.items():
            print(k.upper(), v)

# context
class Pixel:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.pixel_color = color

    def create(self):
        self.pixel_color.create(self.x, self.y)


if __name__ == '__main__':
    factory = FlyweightFactory()
    pixelColor = factory.get_pixel('red')
    pixel = Pixel(10, 10, pixelColor)
    pixel.create()

    pixelColor_2 = factory.get_pixel('red')
    pixel_2 = Pixel(10, 11, pixelColor_2)
    pixel_2.create()

    pixelColor_3 = factory.get_pixel('blue')
    pixel_3 = Pixel(11, 11, pixelColor_3)
    pixel_3.create()

    factory.list_pixel()
