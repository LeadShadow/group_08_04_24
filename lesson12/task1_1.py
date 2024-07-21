import sys

a = {'a': 1, 'b': 2}
if sys.argv[1] == 'update':
    a.update({'c': 3})
    print(a)
elif sys.argv[1] == 'clear':
    a.clear()
    print(a)