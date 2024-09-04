# Завдання 5: Подвоєння чисел і фільтрація результатів
# Опис завдання: У вас є список чисел. Спочатку подвоїте кожне число, а потім створіть
# новий список, що міститиме тільки ті подвоєні числа, які більші за 10.


numbers = [1, 4, 6, 8, 10]
double = map(lambda number: number * 2, numbers)
filter_numbers = list(filter(lambda x: x > 10, list(double)))
print(filter_numbers)
doubled_and_filtered_numbers = list(filter(lambda x: x > 10, map(lambda number: number * 2, numbers)))
# # map(lambda number: numbers * 2, numbers) -> map object(2, 8, 12, 16, 20)
print(doubled_and_filtered_numbers)

