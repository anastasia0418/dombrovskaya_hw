
__author__ = 'Домбровская Анастасия Петровна'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

path = r'C:\Users\I\Desktop\dir_'      # для создания 9 папок
try:
    for i in range(1, 10):
        i = str(i)
        new_path = path + i
        os.mkdir(new_path)
except FileExistsError:
    print("Dirs already exist.")
else:
    print('Dirs were created.')


try:
    for i in range(1, 10):             # для удаления 9 папок
        i = str(i)
        new_path = path + i
        os.rmdir(new_path)
except FileExistsError:
    print("\nCan't delete dirs.")
else:
    print('\nDirs were deleted.')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

os.chdir(r'C:\Users\I\Desktop')
cur_path = os.path.abspath(os.curdir)

def show_dirs(path):  # отображает только папки директории
    all_files = os.listdir(path)
    dirs = []
    for i in all_files:
        if os.path.isdir(i):
            dirs.append(i)
    return dirs


#print('\nHere you can find the following folders: ', show_dirs(cur_path))


def show_files(path):  # отображает все сожержимое директории
    files = os.listdir(path)
    return files


#print('\nFiles in your dir: ', show_files(cur_path))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def duplicate(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)  # copy
        print('\nFile', newfile, 'was created')
    else:
        print("\nWe've got problems =(")


#duplicate('1.py')

