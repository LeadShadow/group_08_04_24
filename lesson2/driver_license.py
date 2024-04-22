# оренда авто

name = 'Sasha'
age = 18
has_driver_license = True
money = 1500

# and, or, not
if name and age >= 18 and has_driver_license and money >= 1000:
    print(f'User {name} can rent a car')

if name:
    if age >= 18:
        if has_driver_license:
            if money >= 1000:
                print(f'User {name} can rent a car')