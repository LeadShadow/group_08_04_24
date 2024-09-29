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
        self.x = x
        self.y = y
