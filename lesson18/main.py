# функція як об'єкт першого класу

def func(x, y):
    return x + y


func_alias = func
result = func_alias(10, 20)
result1 = func(10, 20)
print(result)
print(result1)


def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


def tricky_func(x, y, func):
    return func(x, y)


sum_result = tricky_func(2, 3, sum_func)
print(sum_result)
sub_result = tricky_func(2, 3, sub_func)
print(sub_result)

# області видимості
SOME_VAR = 3


def func(x):
    SOME_VAR = x
    print(SOME_VAR)


def procedure():
    print(SOME_VAR)


procedure()
func(5)
print(SOME_VAR)
# ----------------------------------------------------------

SOME_VAR = 3


def func(x):
    global SOME_VAR
    SOME_VAR = x
    print(SOME_VAR)


def procedure():
    print(SOME_VAR)


procedure()
func(5)
print(SOME_VAR)
print('--------------------------------------------------------------------------------')
# y = 15
#
#
# def func():
#     x = 14
#
#     def func1():
#         x1 = 13
#
#         def func2():
#             x2 = 12
#
#             def func3():
#                 x3 = 11
#
#                 def func4():
#                     x4 = 10
#                     print(y)


# Замикання

def adder(value):
    def inner(x):
        return x + value
    return inner


two_adder = adder(2)
print(two_adder(3))

print('--------------------------------------------------------------------------------')

# карінг -> каррування

def handle_operator(x, y, operator):
    if operator == '-':
        return x - y
    if operator == '+':
        return x + y


print(handle_operator(10, 20, '-'))
print(handle_operator(10, 20, '+'))

def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}

def handle_operator(operator):
    return OPERATIONS[operator]

result = handle_operator('-')
print(result(10, 20))

print('--------------------------------------------------------------------------------')

# декоратори


def complicated(x, y):
    return x / y


def logged_func(func: complicated):
    def inner(x, y):
        print(f'Called with {x}, {y}')
        result = None
        try:
            result = func(x, y)
        except ZeroDivisionError:
            print('Ділення на нуль неможливе')
        except TypeError:
            print('dawdaw')
        except ValueError:
            print('dawda')
        print(f'result: {result}')
        return result
    return inner


complicated = logged_func(complicated)
complicated(10, 0)


@logged_func
def complicated(x, y):
    return x / y


complicated(10, 0)

# ітератори, генератори, лямбда функції(анонімні функції), map, filter + якісь приклади завдань

