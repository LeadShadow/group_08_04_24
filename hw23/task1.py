# У класу Point через конструктор __init__ оголошено два атрибути:
# координати x та y. Приховати доступ до них з допомогою подвійного підкреслення: __x та __y
#
# Реалізуйте для класу Point механізми setter та getter до атрибутів
# __x та __y за допомогою декораторів property та setter.
#
# Приклад:
#
# point = Point(5, 10)
#
# print(point.x)  # 5
# print(point.y)  # 10

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


p = Point(10, 20)
print(p.x)
p.x = 20
print(p.x)
print(p.y)
p.y = 'hello'
print(p.y)
