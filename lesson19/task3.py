# Завдання 3: Збільшення кожного числа на 5
# Опис завдання: У вас є список чисел. Вам потрібно створити новий список, в якому
# кожне число збільшено на 5.

numbers = [10, 20, 30, 40, 50]
increased_numbers = list(map(lambda number: number + 5, numbers))
print(increased_numbers)


def func1(numbers):
    increased_numbers = []
    for i in numbers:
        increased_numbers.append(i + 5)
    return increased_numbers


print(func1(numbers))
