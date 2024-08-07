from datetime import datetime, timedelta

current_datetime = datetime.now()
print(current_datetime)

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

print(current_datetime.date())
print(current_datetime.time())

d1 = datetime(year=2012, month=1, day=5, hour=14)

print(d1.weekday())
a = {
    0: 'Понеділок',
    1: 'Вівторок',
    2: 'Середа',
    3: 'Четвер',
    4: "П'ятниця",
    5: 'Субота',
    6: 'Неділя',
}
print(f'Це {a[d1.weekday()]}')

current_datetime = datetime.now()

future_month = (current_datetime.month % 12) + 1
future_year = current_datetime.year + int(current_datetime.month / 12)
future_datetime = datetime(future_year, future_month, 1)
print(future_datetime)
print(future_datetime - current_datetime)

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(type(difference))
print(difference)
print(difference.total_seconds())

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
seventh_day_2021 = datetime(year=2021, month=1, day=7, hour=14)

difference = seventh_day_2021 - seventh_day_2020
print(difference)
print(difference.total_seconds())

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
seventh_day_2020_1 = datetime(year=2020, month=2, day=4, hour=14)
print(seventh_day_2020_1 - seventh_day_2020)
four_weeks_interval = timedelta(weeks=4)
print(seventh_day_2020 + four_weeks_interval)


delta = timedelta(days=20, hours=10, minutes=10, microseconds=20, weeks=2, seconds=40, milliseconds=100)
print(delta)

user_input = '2024-09-01:10:10:10'  # рядки str
print(type(user_input))
a = input('Введіть число: ')
print(type(int(a)))  # '10'


seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.strftime('%A/%d/%B/%Y'))

s = input('Введіть дату в наступному форматі(день-місяць(словом)-рік): ')
try:
    print(datetime.strptime(s, '%d-%B-%Y'))
except ValueError:
    try:
        print(datetime.strptime(s, '%d %B %Y'))
    except ValueError:
        print('Формат взагалі не підходить')

