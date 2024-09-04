# Завдання 1: Перетворення рядків у великі літери
# Опис завдання: У вас є масив рядків. Вам потрібно створити новий масив, в якому всі рядки
# будуть перетворені на великі літери.


words = ['apple', 'banana', 'orange']  # -> ['APPLE', 'BANANA', 'ORANGE']
upper_case_words = list(map(lambda word: word.upper(), words))
print(upper_case_words)