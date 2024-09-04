# Завдання 2: Фільтрація парних чисел
# Опис завдання: У вас є список чисел. Вам потрібно створити новий список, що
# міститиме тільки парні числа з оригінального списку.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)


def func1(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


print(func1(numbers))
