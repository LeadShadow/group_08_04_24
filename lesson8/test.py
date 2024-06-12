# get метод словника

chars = {'a': 1, 'b': 2}
c_index = chars.get('b', -1)
print(c_index)

numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}

for key in numbers:
    print(key)


print('------------------------------------------')
for key in numbers.keys():
    print(key)


print('------------------------------------------')
for value in numbers.values():
    print(value)


print('------------------------------------------')
for key, value in numbers.items():
    print(key, value)


# key, value = (1, 'one')
# [1, 2, 3, 4]
# numbers = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }
# {1, 2, 3, 4, 5}
# (1, 2, 3, 4, 5)

# Множини
a = set()
print(type(a))

a = set('hello')
print(a)

# add(elem)
numbers = {1, 2, 3}
numbers.add(4)
numbers.add(4)
print(numbers)


# remove(elem)
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)


# discard(elem)
numbers = {1, 2, 3}
numbers.discard(4)
print(numbers)


# рядки
print('didn\'t')
print("didn't")

s = 'Hello world'
print(s[0])
print(s[-1])

# s[0] = 'Q'

# методи рядків

# .upper()
s = 'Hello!'
s = s.upper()  # s.upper() -> повертає всі великі літери в рядку, але не змінює сам рядок
print(s)

# .lower()
s = 'HELLO!'
s = s.lower()  # s.lower() -> повертає всі маленькі літери в рядку, але не змінює сам рядок
print(s)

# .startswith()
s = '+380937316049'
if s.startswith('+380'):
    print('цей номер український')

# .endswith()
# png, jpg, jpeg, svg
s = 'hello.png'
if s.endswith('.jpg') or s.endswith('.png') or s.endswith('.jpeg') or s.endswith('.svg'):
    print('це фотографія!')

if 'hello' in s:
    print('dwadaw')

print(len(s))