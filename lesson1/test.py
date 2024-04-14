# змінні
age = 18

# 1 ім'я змінної в пайтоні може бути тільки з цифр, букв і знаків _
# @$%
hello_world = "hello world"
# 2 ім'я змінної не може починатись з цифри, але може з _
_a = 20
# 3 використання зарезервованих слів в якості назви змінної призведе до помилки
# if, elif, else, True, False, None. or, and

# оператори і операнди
# + - * / % // **
# 8 ** 2 -> 8 * 8
x = 8 ** 2 + 4 * (2 + 2)
# 80
print(x)

# Типи данних
# 1 None -> пусте значення і ніякий тип даних
# 2 Числа
# 3 Boolean -> булевий(логічний тип) є підтипом цілих чисел -> True or False
# 4 Рядки

a = None
print(a)
a = 10
print(a)

int_number = 10
float_number = 7.62
complex_number = 3.3 + 3j

print(int_number + float_number + complex_number)

hello_string = 'Hello'
world_string = "World"

print(hello_string + ' ' + world_string)  # Hello World
print(f'{hello_string} {world_string}')

# print('I didn't do it')  Не робити цього!
print("I didn't do it")
print('I didn\'t do it')  # \' -> апостроф

# Boolean

# 1
a = True
b = False

# 2
age = 18
adult1 = age >= 18  # age >= 18 -> True

age = 15
adult2 = age >= 18  # False

print(adult1, adult2)

# print -> виводить на екран те шо ми прокинемо їй в круглих дужках
print('Hello world')

# input -> введення даних з консолі
a = input('Введіть щось: ')
print(type(a))  # type(object) -> повертає тип об'єкта який ми прокинемо в дужках
# 10, '10'

x = int(input('Введіть перше число: '))  # 'dawdwadaw' -> 10
y = int(input('Введіть друге число: '))

print(x + y)