# 9. Класи
# Задача: Створіть клас Rectangle, який приймає довжину та ширину. Додайте методи для
# обчислення площі та периметра прямокутника. Створіть об'єкт і протестуйте методи.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


def test_rectangle():
    rect = Rectangle(5, 2)
    print(f'Площа: {rect.area()}')
    assert 10 == rect.area()
    print(f'Периметр: {rect.perimeter()}')
    assert 14 == rect.perimeter()


test_rectangle()