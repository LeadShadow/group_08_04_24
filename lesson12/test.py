# pathlib
from pathlib import Path
import sys

p = Path()
print(p.parent)
print(p.name)
print(p.suffix)

print(p.exists())
print(p.is_dir())
print(p.is_file())
print(p.iterdir())
print(range(1, 12))

for i in p.iterdir():
    print(i.name)

print('--------------------------------------------')
# обробка аргументів командного рядка
print(sys.argv)