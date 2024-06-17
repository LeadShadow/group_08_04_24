# спеціальні символи рядків
# \n -> перенесення рядка
# \f -> перенесення сторінки
# \r -> повернення каретки
# \t -> горизонтальна табуляція
# \v -> вертикальна табуляція
print("dawdawdawdaw\rhello world")
print("dawdawdawdaw\nhello world")

# методи рядків
# пошук в рядку
s = 'Hi there!'
start = 0
end = 8
print(s.find('er'))
print(s.find('q'))

s = 'I am learning strings in Python. Some new methods got now.'
sentences = s.split('. ')
print(sentences)

text = '. '.join(sentences)
print(text)

clean = '            hello              '
print(clean)
clean = clean.strip()
print(clean)

dogs_text = 'All dogs bark like dogs.'
cats_text = dogs_text.replace('dogs', 'cats')
print(cats_text)

print('TestHook'.removeprefix('Test'))
print('TestHook'.removeprefix('Hook'))

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))
