# Завдання: Напишіть програму, яка перевіряє, чи є введений рядок дійсним
# українським мобільним номером телефону. Український мобільний номер має
# наступний формат: +380xxxxxxxxx, де x - це цифра від 0 до 9, інші символи
# не допускаються.
#
# Приклад вхідних даних:
#
# "+380971234567"
# "380661234567"
# "+380 (50) 123-45-67"
# "123456789"
import re

phone_numbers = [
    "+380971234567",
    "380661234567",
    "+380 (50) 123-45-67",
    "123456789",
    "0937316049",
    '0501243567'
]

def validate_ukrainian_phone_number(phone_number: str):
    phone_number = re.sub('-|\(|\)| ', '', phone_number)
    pattern = r'^(\+380|380|0)\d{9}$'
    return bool(re.match(pattern, phone_number))


for number in phone_numbers:
    print(validate_ukrainian_phone_number(number))
