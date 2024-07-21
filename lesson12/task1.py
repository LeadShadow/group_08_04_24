# написати функцію яка буде парсити папку і повертати списки
# 1-й список це список файлів всередині папки
# 2-й список це список папок всередині папки
from pathlib import Path

def parse_folder(path: Path):
    files = []
    folders = []
    for element in path.iterdir():
        if element.is_file():
            files.append(element.name)
        elif element.is_dir():
            folders.append(element.name)
    return files, folders


if __name__ == "__main__":
    print(parse_folder(Path('C:/Users/pc/Desktop/заняття/group_08_04_24/lesson12')))