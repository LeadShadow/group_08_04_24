# Клас Rectangle
# Створіть клас Rectangle, що представляє прямокутник.
#
# Завдання:
#
# Реалізуйте метод __init__, щоб приймати ширину та висоту.
# Реалізуйте метод area, щоб обчислювати площу.
# Реалізуйте метод __str__, щоб виводити розміри прямокутника.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


rectangle = Rectangle(5, 10)
print(rectangle)
print(rectangle.area())
