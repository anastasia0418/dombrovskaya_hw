
__author__ = 'Домбровская Анастасия Петровна'

import os, sys

def create_dir(path):  # создаем папку
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Dir already exists.")
    else:
        print('Dir was created successfully.')

def del_dir(path):  # удаляем папку
    try:
        os.rmdir(path)
    except FileExistsError:
        print("Dir has already been deleted.")
    else:
        print('Dir was deleted successfully.')

def show_files(path):  # отображает все сожержимое директории
    files = os.listdir(path)
    return files

def show_dirs(path):  # отображает только папки директории
    all_files = os.listdir(path)
    dirs = []
    for i in all_files:
        if os.path.isdir(i):
            dirs.append(i)
    return dirs