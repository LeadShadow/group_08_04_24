# Завдання 4: Фільтрація коротких рядків
# Опис завдання: У вас є список рядків. Вам потрібно створити новий список, що
# міститиме тільки ті рядки, довжина яких менша ніж 5 символів.


strings = ['apple', 'fig', 'banana', 'kiwi', 'grape']

short_strings = list(filter(lambda string: len(string) < 5, strings))
print(short_strings)


def func1(strings):
    short_strings = []
    for i in strings:
        if len(i) < 5:
            short_strings.append(i)
    return short_strings


print(func1(strings))