# 1. Основні типи даних в Python
# Задача: Напишіть програму, яка приймає від користувача число (float), ціле число
# (int), рядок (str) та булеве значення (bool). Виведіть їх типи та значення на екран.
float_num = float(input('Введіть число: '))
int_num = int(input('Введіть число: '))
string_value = input('Введіть рядок: ')
bool_value = input('Введіть булеве значення (True/False): ') == "True"

print(float_num, int_num, string_value, bool_value)
print(type(float_num), type(int_num), type(string_value), type(bool_value))
