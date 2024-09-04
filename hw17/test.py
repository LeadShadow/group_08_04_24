# Завдання: Підрахунок частоти слів у списку
# Опис Завдання:
# Створіть програму, яка приймає список слів і підраховує, як часто кожне слово
# з'являється у цьому списку. Результат має бути у вигляді списку об'єктів namedtuple,
# де кожен об'єкт містить слово та його частоту.
#
# Вимоги:
#
# Використовуйте namedtuple для зберігання слова і його частоти.
# Створіть словник для підрахунку частоти слів.
# Виведіть результат у вигляді списку namedtuple.
# Приклад Вхідних Даних:
#
# Список слів: ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# Приклад Виходу:
#
# [
#     WordFrequency(word='apple', frequency=3),
#     WordFrequency(word='banana', frequency=2),
#     WordFrequency(word='orange', frequency=1)
# ]
import pprint
from collections import namedtuple

# 1 створення іменованого кортежу
WordFrequency = namedtuple('WordFrequency', ['word', 'frequency'])
list_of_fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']


def func(word_list):
    word_counts = {}
    # 2 створення словника для підрахунку частоти слів
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # 3 створення списку namedtuple, з результатами
    result = []
    for word, count in word_counts.items():
        result.append(WordFrequency(word=word, frequency=count))

    return result


pprint.pprint(func(list_of_fruits))
