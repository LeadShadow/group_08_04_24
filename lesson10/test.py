import re
# форматування рядків
# логування - виведення результатів в консоль
for num in range(12):
    print('{:^10} | {:^10} | {:^10}'.format(num, num ** 2, num ** 3))


print('-' * 200)
print('{:^149}'.format(10 + 20))
print('-' * 200)
print('{:>150}'.format(10 * 20))

a = 'Sasha'
print(f'Hello, {a}')
print('Hello, {}'.format(a))

# регулярні вирази
print('-' * 200)
s = 'I am 19 years old 54358348 53485834858 3 54385 834'
age = re.search('[0-9]+', s)  # \d - цифра, [0-9]
print(age.group())
numbers = re.findall('\d+', s)
print(numbers)

dogs_text = 'All dogs bark like dogs.'
cats_text = re.sub("dogs", "cats", dogs_text)
print(cats_text)

p = re.sub('(blue|white|red)', 'colour', 'blue socks and red shoes')
print(p)

s = '74327 547375734 547537547 537457347 hello_world'
s1 = re.sub('\d+', '', s).strip()
print(s1)
