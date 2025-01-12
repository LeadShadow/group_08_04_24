# 3. Робота з функціями
# Задача: Напишіть функцію factorial(n), яка приймає ціле число
# n і повертає його факторіал. Перевірте функцію для кількох значень
# n, включаючи 0


# 5! = 1 * 2 * 3 * 4 * 5 -> 5 * 4! -> 5 * 4 * 3!
def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


numbers = [0, 1, 5, 10]
for num in numbers:
    print(f'Факторіал {num}: {factorial(num)}')

