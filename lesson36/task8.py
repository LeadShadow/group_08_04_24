# 8. Робота з функціями (поглиблена)
# Задача: Напишіть функцію apply_operations, яка приймає список чисел і будь-яку кількість
# функцій. Функція повинна послідовно застосовувати всі передані функції до кожного
# елемента списку.

def square(x):
    return x ** 2


def increment(x):
    return x + 1


def apply_operations(numbers: list, *operations):
    for operation in operations:
        # [1, 2, 3, 4, 5]
        numbers = [operation(num) for num in numbers]
        # [1, 4, 9, 16, 25]
        # [2, 5, 10, 17, 26]
    return numbers


numbers = [1, 2, 3, 4, 5]
result = apply_operations(numbers, square, increment)
print('результат: ', result)
