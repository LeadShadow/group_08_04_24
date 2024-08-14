# Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі
# ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 'Thursday 27 May 2021'
# - день тижня, число, місяць та рік. Перетворене значення функція повертає під час виклику.

from datetime import datetime


def get_str_date(date: str):
    date1 = datetime.strptime(date[:-1], '%Y-%m-%d %H:%M:%S.%f')
    return date1.strftime('%A %d %B %Y')


print(get_str_date('2021-05-27 17:08:34.149Z'))
