import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
OTHER = []
ARCHIVES = []
AVI_VIDEO = []
MP4_VIDEO = []
MKV_VIDEO = []
MOV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
CSV_DOCUMENTS = []
FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'PNG': PNG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'ZIP': ARCHIVES,
    'MP4': MP4_VIDEO,
    'MKV': MKV_VIDEO,
    'MOV': MOV_VIDEO,
    'AVI': AVI_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'CSV': CSV_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS
}

# 'text.txt' -> 'TXT'
# 'text.txt' -> '.txt'
def get_extensions(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


# item -> C:\Users\pc\Desktop\заняття\group_08_04_24\lesson13\file_parser.py
def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # якшо це папка то додаємо її в список FOLDERS, і переходимо до наступного елементу
        if item.is_dir():
            # перевіряємо шоб ця папка не була тою в яку ми складаємо файли
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                # скануємо вложену папку(рекурсія)
                scan(item)
            continue

        # пішла робота з файлом
        ext = get_extensions(item.name)
        fullname = folder / item.name
        if not ext:
            OTHER.append(fullname)
        else:
            try:
                # взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == "__main__":
    folders_for_scan = sys.argv[1]
    print(f'Start in folder: {folders_for_scan}')
    scan(Path(folders_for_scan))

    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Images PNG: {PNG_IMAGES}')

    print(f'Documents TXT: {TXT_DOCUMENTS}')
    print(f'Documents DOC: {DOC_DOCUMENTS}')
    print(f'Documents PDF: {PDF_DOCUMENTS}')