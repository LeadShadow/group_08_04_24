import shutil

archive_name = shutil.make_archive('backup', 'zip')

shutil.unpack_archive(archive_name, 'new_folder')