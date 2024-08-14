# Напишіть функцію визначення кількості днів у конкретному місяці.
# Ваша функція повинна приймати два параметри: month - номер місяця у вигляді
# цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр.
# Перевірте, чи функція коректно обробляє місяць лютий високосного року.

from datetime import date, datetime


def get_days_in_month(month: int, year: int):
    day1 = datetime(year=year, month=month, day=1)
    day2 = datetime(year=year+1, month=1, day=1) if month == 12 else datetime(year=year, month=month + 1, day=1)
    return (day2 - day1).days

# 2024-12-1
# 2025-01-01
print(get_days_in_month(2, 2024))

