# структури даних - колекції

# впорядкованість
# змінність
# унікальність

# списки

my_list = []

another_list = list()

print(my_list, another_list)

not_empty = [1, 2, 3, 4, 'mam']
print(not_empty)


some_iterable = ['a', 'b', 'c']
first_letter = some_iterable[0]
second_letter = some_iterable[1]
third_letter = some_iterable[2]
print(first_letter)
print(second_letter)
print(third_letter)
print(some_iterable)


some_iterable = ['a', 'b', 'c']
first_letter = some_iterable[-1]
second_letter = some_iterable[-2]
third_letter = some_iterable[-3]
print(first_letter)
print(second_letter)
print(third_letter)
print(some_iterable)


some_iterable = ['a', 'b', 'c']
some_iterable[1] = 'x'
print(some_iterable)

# зрізи
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]
print(odd_numbers, even_numbers, three_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2::3]
print(odd_numbers, even_numbers, three_numbers)

print(numbers[0:3])

numbers_copy = numbers[:]
print(numbers_copy)
numbers_copy.append(1)
print(numbers)


# append - добавляє елемент в кінець
chars = ['a', 'b']
chars.append([1, 2, 3])
print(chars)

# clear - очищує список

nums = [1, 2, 3, 4]
nums.clear()
print(nums)


# remove - видаляє об'єкт вказавши ім'я об'єкту
chars = ['a', 'b']
chars.remove('b')
print(chars)


# pop - видаляє елемент по індексу
chars = ['a', 'b']
# chars.pop(5)
print(chars)

# extend - розширення списка іншим списком
chars = ['a', 'b']
nums = [1, 2, 3]
chars.extend(nums)
print(chars)


# insert
chars = ['a', 'b']
chars.insert(1, 'c')
print(chars)

# .index('c'), .count('a')

chars = ['x', 'a', 'b']
chars.sort(reverse=True)
print(chars)

nums = [1, 2, 3, 432, 10, 3, 2, 129, 5]
nums.sort(reverse=True)
print(nums)


nums.reverse()


# словники
# Саша - +380937316049
a = {'Саша': '+380937316048'}

# pop(key) - видалення пари ключ-значення по ключу
chars = {'a': 1, 'b': 2}
chars.pop('a')
print(chars)

# copy, clear

chars = {'a': 1, 'b': 2}
chars1 = {'c': 3}
chars.update(chars1)
print(chars)