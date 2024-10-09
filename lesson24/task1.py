# У класу Point до механізму setter властивостей x і y додайте перевірку на
# значення, що вводиться. Дозвольте встановлювати значення властивостей x та y для
# екземпляра класу, тільки якщо вони мають числове значення (int або float).
#
# Приклад:
#
# point = Point("a", 10)
#
# print(point.x)  # None
# print(point.y)  # 10

class IncorrectInputType(Exception):
    def __str__(self):
        return 'Incorrect type of variable'


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in (int, float):
            self.__x = x
        else:
            raise IncorrectInputType

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__x = y


p = Point(10, 20)
print(p.x)
p.x = 'Hello'
print(p.x)