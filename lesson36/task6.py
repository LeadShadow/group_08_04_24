"""
Створює текстовий файл data.txt і записує в нього рядки, введені користувачем,
поки він не введе слово "STOP".
Зчитує файл і виводить його вміст у зворотному порядку рядків.
"""

with open('data.txt', 'w') as file:
    while True:
        line = input('Введіть рядок (або STOP для завершення): ')
        if line.upper() == 'STOP':
            break
        file.write(line + '\n')


with open('data.txt', 'r') as file:
    lines = file.readlines()


print('Рядки у зворотньому порядку: ')
for line in reversed(lines):
    print(line.strip())
