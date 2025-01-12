# 11. Серіалізація та десеріалізація (pickle, json)
# Задача: Напишіть програму, яка:
#
# Створює словник із інформацією про користувача (ім'я, вік, хобі).
# Зберігає цей словник у файлі у форматі JSON.
# Зчитує файл і виводить вміст на екран у форматі Python-словника.
import json

user_data = {
    'name': 'Oleksandr',
    'age': 20,
    'hobbies': ['football', 'music', 'programming'],
}

with open('user_data.json', 'w') as file:
    json.dump(user_data, file)


with open('user_data.json', 'r') as file:
    loaded_data = json.load(file)


print('Завантажені файли:', loaded_data)
assert user_data == loaded_data
