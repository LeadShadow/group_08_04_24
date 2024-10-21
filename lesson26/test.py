import csv
import copy

with open('eggs.csv', 'w', newline='') as file:
    spam_writer = csv.writer(file)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


with open('eggs.csv', 'r', newline='') as file:
    spam_reader = csv.reader(file)
    for row in spam_reader:
        print(','.join(row))


with open('names.csv', 'w', newline='') as file:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Oleksandr', 'last_name': 'Samus'})
    writer.writerow({'first_name': 'Masha', 'last_name': 'Kondratuyk'})
    writer.writerow({'first_name': 'Misha', 'last_name': 'Lebiga'})


with open('names.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['first_name'], row['last_name'])


# створення копій об'єктів в Пайтоні

my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list)

my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list)

my_list = [1, 2, 3]
copy_list = my_list.copy()
copy_list.append(4)
print(my_list)

my_list = [1, 2, 3, {1: 'a'}]
copy_list = copy.deepcopy(my_list)
copy_list[3][2] = 'b'
print(copy_list)
print(my_list)

