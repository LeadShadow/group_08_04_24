# 5. Робота з рядками (поглиблена)
# Задача: Напишіть функцію, яка приймає рядок та повертає словник, де ключами є символи,
# а значеннями – кількість їх входжень у рядок. Ігноруйте регістр символів.


def char_count(s: str):
    s = s.lower()
    counts = {}
    for char in s:
        if char.isalnum():
            counts[char] = counts.get(char, 0) + 1
    return counts


string = input('Введіть рядок: ')
print('Кількість символів у рядку: ', char_count(string))
