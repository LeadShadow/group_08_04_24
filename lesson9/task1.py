# Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних
# керівних символів: [\n, \f, \r, \t, \v]
#
# Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
#
# 'Alex\nKdfe23\t\f\v.\r' -> 11
# 'Al\nKdfe23\t\v.\r'

def real_len(text):
    special_chars = ['\n', '\f', '\r', '\t', '\v']
    count = 0
    for char in text:
        if char not in special_chars:
            count += 1
    return count

s1 = 'Alex\nKdfe23\t\f\v.\r'
print(real_len(s1))


def real_len(text):
    special_chars = ['\n', '\f', '\r', '\t', '\v']
    for char in text:  # 'Alex\nKdfe23\t\f\v.\r'
        if char in special_chars:
            text = text.replace(char, '')  # 'AlexKdfe23\t\f\v.\r'
    return len(text)

s1 = 'Alex\nKdfe23\t\f\v.\r'
print(real_len(s1))