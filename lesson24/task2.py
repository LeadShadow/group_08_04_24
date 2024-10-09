# Реалізуйте клас Vector. Властивість coordinates визначає координати вектора
# і є екземпляром класу Point. Нагадаємо, що вектором називають спрямований відрізок
# з початком та кінцем. Початок у нас буде в точці (0, 0), а кінець вектора ми
# задаватимемо атрибутом coordinates.
#
# Реалізуйте можливість звертатися до координат екземпляра класу Vector через квадратні дужки:
#
# vector = Vector(Point(1, 10))
#
# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10
#
# vector[0] = 10  # Встановлюємо координату x вектора 10
#
# print(vector[0])  # 10
# print(vector[1])  # 10
# Щоб отримати значення, використовуючи квадратні дужки об'єкта print(vector[0]),
# реалізуйте метод __getitem__ у класу Vector.
#
# Для запису значення координат вектора через індекс, як vector[0] = 10, реалізуйте метод __setitem__ у класу Vector.
#
# Звернення до координати x проводиться за індексом 0, а звернення до координати
# y - за індексом 1.
