# 10. Магічні методи класів
# Задача: Створіть клас Vector для роботи з векторами в 2D-просторі. Реалізуйте
# магічні методи:
#
# __add__ – додавання векторів;
# __sub__ – віднімання;
# __mul__ – скалярний добуток;
# __repr__ – представлення вектора у вигляді Vector(x, y).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def sum(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)


    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


v1 = Vector(2, 2)
v2 = Vector(3, 4)
print(f'Сума:', v1 + v2)
print(f'Різниця:', v1 - v2)
print(f'Добуток:', v1 * v2)
print(v1.sum(v2))