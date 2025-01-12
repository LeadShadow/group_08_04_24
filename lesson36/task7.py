# 7. Пакет random
# Задача: Напишіть програму, яка генерує випадковий список із 10 чисел у діапазоні від
# 1 до 100. Знайдіть мінімальне, максимальне значення та їх індекси у списку.
import random

random_numbers = [random.randint(1, 100) for _ in range(10)]

min_value = min(random_numbers)
max_value = max(random_numbers)
min_index = random_numbers.index(min_value)
max_index = random_numbers.index(max_value)

print('Випадкові числа: ', random_numbers)
print(f'Мінімум: {min_value}, індекс {min_index}')
print(f'Максимум: {max_value}, індекс {max_index}')