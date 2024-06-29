# робота з файлами
file = open('test_file.txt')
# 'r' -> відкриття на читання(значення за замовчуванням)
# 'w' -> відкриття на запис, якщо файлу не існує, то створить його і запише туди інформацію
# 'x' -> відкриття на запис, якшо файлу не існує то буде виняток
# 'a' -> відкриття на дозапис
# 'b' -> відкриття в двійковому режимі
# '+' -> відкриття на читання та запис
file.close()

fh = open('test_file.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)
file.close()

# читання та запис у файл
fh = open('test_file.txt', 'w+')
fh.write('hello!')
fh.seek(0)
first_two_symbols = fh.read(2)
print(first_two_symbols)
file.close()

fh = open('test_file.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test_file.txt', 'r')
all_file = fh.read()
print(all_file)
fh.close()

fh = open('test_file.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test_file.txt', 'r')
while True:
    symbol = fh.read(1)
    if not symbol:
        break
    print(symbol)

fh.close()

fh = open('test_file.txt', 'w')
fh.write('first_line\nsecond_line\nthird_line')
# first_line
# second_line
# third_line
fh.close()

fh = open('test_file.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

fh = open('test_file.txt', 'w')
fh.write('first_line\nsecond_line\nthird_line')
# first_line
# second_line
# third_line
fh.close()

fh = open('test_file.txt', 'r')
lines = fh.readlines()
print(lines)
fh.close()

# менеджер контекста
# fh = open('test_file.txt')
# try:
#     some_function(fh)
# finally:
#     fh.close()


with open('test_file.txt', 'w+') as file:
    some_function(file)


# робота з архівами
