# try-except
# 3 винятки -> виконання блоку інструкцій в випадку помилки

value = '10'
try:
    value = int(value)
    print(value > 0)
except ValueError:
    print(f'value {value} is not a number')
finally:
    print('This will be printed anyway')

age = input('How old are you?: ')
try:
    age = int(age)
    if age >= 18:
        print('You are adult.')
    else:
        print('You are infant')
except ValueError:
    print(f'{age} is not a number')

# функції
def say_hello():
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')
    print('Hello!')


say_hello()

print('-------------------------')

say_hello()

print('-------------------------')

say_hello()

# аргументи функції

def print_max(a, b):
    if a > b:
        print(f'a == {a}, максимальне')
    elif a == b:
        print('a == b')
    else:
        print(f'b == {b}, максимальне')


print_max(a=10, b=10)

# локальний простір це простір всередині функції, все шо буде в ньому визначено,
# буде недоступним за межами цієї функції
# глобальний простір це простір за межами функції


def plus(a, b):
    return a + b


print(plus(3, 4))

x = 50

def func():
    x = 2
    print(f'Заміна глобального х на {x}')

func()
print(f'х все ще {x}')

x = 50

def func():
    global x
    print(f'x == {x}')  # x == 50
    x = 2
    print(f'Замінюємо глобальне значення x на {x}')  # 2

func()
print(f'Значення тепер x == {x}')


x = 50

def func():
    x = 2
    print(f'Замінюємо глобальне значення x на {x}')  # 2
    return x

x = func()  # func() -> 2
print(f'Значення тепер x == {x}')