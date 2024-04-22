# 1 умовне виконання -> виконання блоку інструкцій тільки при наступленні якоїсь умови
# 2 цикли -> повторення виконання блоку інструкцій, поки виконується якась умова
# 3 винятки -> виконання блоку інструкцій в випадку помилки

# int('dawdawdawdaw') -> ValueError

age = int(input('How old are you?: '))  # '18' -> 18

# Умовне виконання
if age >= 18:
    # '18' >= 18  -- 18 >= 18  True
    print('You are adult already')
else: # if age < 18
    print('You are infant yet')



a = int(input('Введіть число: ')) # якшо ми ввели нуль то виконається else

if a > 0:
    print('Число додатнє')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число нуль')


a = int(input('Введіть число: '))

if a > 0:  # a > 0 -> True or False
    print('Число додатнє')
else:
    print('a <= 0')


# bool
money = 0  # False
if money:
    print(f'You have {money} on your bank account')
else:
    print('You have no money')

print(bool(0))  # False
print(bool(None))  # False

# None -> False
result = None
if result:
    print(result)
else:
    print('Result is None')

# '' -> False
user_name = input('Enter your name: ')
if user_name:
    print(f'Hello {user_name}')
else:
    print('Hello anonim!')


# and(I) -> *  True(1) * True(1) -> 1 * 1 -> 1
# a     b     a and b
# True  True    True
# True  False   False  True(1) * False(0) -> 1 * 0 -> 0(False)
# False True    False
# False False   False

# or(або) -> True(1) + True(1) -> 1 + 1 -> 1
# a      b      a or b
# True   True    True
# True   False   True  True(1) + False(0) -> 1 + 0 -> 1
# False  True    True
# False  False   False

# not(ні) -> заперечення
# not True -> False
# not False -> True


# тернарний оператор
is_nice = True
state = 'nice' if is_nice else 'not nice'
print(state)
state = ''
if is_nice:
    state = 'nice'
else:
    state = 'not nice'
print(state)