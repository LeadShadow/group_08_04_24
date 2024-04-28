# цикли
# for, while

# for -> це ітеруючий цикл, він перебирає всі елементи послідовності
fruit = 'apple'
for char in fruit:
    print(char)

for i in range(1, 10):  # 1, 10 -> 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(i)


# цикл while -> це цикл який виконується поки виконується якась умова
a = 1
while a <= 5:
    print(a)
    a += 1


# Безкінечний цикл
a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1


while True:
    user_input = input('Введіть щось: ')
    print(user_input)
    if user_input == 'exit':  # точка виходу
        break
