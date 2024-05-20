# ключеві аргументи
from math_test import say_hello
def func(a, b=5, c=10):
    print(f'a == {a}, b == {b}, c == {c}')


func(10)
func(20, 15, 25)
func(a=20, b=25, c=30)


# змінна к-сть параметрів
def total(a=5, *numbers, **phone_book):
    print(f'a == {a}')

    for item in numbers:
        print(f'item == {item}')

    for first, second in phone_book.items():
        print(first, second)


# 1, 12, 3, 4, 5, 6 -> (1, 12, 3, 4, 5, 6)
# Sasha='+380937316048', Misha='+380937316048' -> {'Sasha': '+380937316048', 'Misha': '+380937316048'}
# Славік - +380937316048
total(10, 1, 12, 3, 4, 5, 6, Sasha='+380937316048', Misha='+380937316048')

# контейнери(колекції)
# кортеж
my_tuple = tuple()
another_my_tuple = ()
print(my_tuple, another_my_tuple)

not_empty = (1, 2, 3)

print(not_empty[0])
print(not_empty[1])
print(not_empty[2])

print(not_empty)

# словник
# hello = 'hello '
# world = 'world'
# print(hello + world)
empty_dict = {}
another_empty_dict = dict()

some_dict = {
    'key': 'value',
    1: 'one',
    2: 'two',
    3: 'three'
}

not_empty_dict = {'key': 'value'}
not_empty_dict['new_key'] = 'new_value'


say_hello()