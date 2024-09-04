for i in range(1, 10):
    print(i)


def interval_generator(x, y):
    while x < y:
        yield x
        x += 1


one_to_ten = interval_generator(1, 10)
# for i in one_to_ten:
#     print(i)


print(next(one_to_ten))
print(next(one_to_ten))


# лямбда функції(анонімні функції)
def sum_lambda(x, y):
    return x + y


print(sum_lambda(2, 3))

sum_lambda = lambda x, y: x + y

print(sum_lambda(2, 3))

kvadrat_num = lambda x: x ** 2

print(kvadrat_num(5))

# map
numbers = [1, 2, 3, 4, 5]

a = map(lambda x: x ** 2, numbers)
for i in a:
    print(i)


def kvadrat_nums(numbers: list):
    for i in numbers:
        print(i ** 2)


kvadrat_nums(numbers)

# filter

for i in filter(lambda x: x % 2 == 1, range(1, 12)):
    print(i)


def func1(range_):
    for i in range_:
        if i % 2 == 1:
            print(i)


func1(range(1, 12))

# на наступному занятті будем розглядати консольного бота
