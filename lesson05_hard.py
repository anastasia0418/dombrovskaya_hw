# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создать копию файла")
    print("rm <file_name> - удалить указанный файл")
    print("cd <full_path or relative_path> - поменять текущую директорию")
    print("ls - отобразить полный путь текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def duplicate():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    #dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(dir_name):
        try:
            newfile = dir_name + '.dupl'
            shutil.copy(dir_name, newfile)  # copy
            print(newfile, 'создан')
        except OSError:
            print('Неудалось скопировать файл')
    else:
        print('Файл не найден')


def delete():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    #dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(dir_name):
        answer = input('Удалить файл? (Да/Нет) ')
        answer = answer.islower()
        if answer == 'да':
            try:
                os.remove(dir_name)
                print(dir_name, ' удален')
            except OSError:
                print('Неудалось удалить файл')
        elif answer == 'нет':
            print('Отмена удаления')
    else:
        print('Файл не найден')


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.chdir(dir_path)
    cur_path = os.path.abspath(os.curdir)
    print('Ваша директория теперь: ', cur_path)


def full_path():
    fp = os.getcwd()
    print(fp)


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": duplicate,
    "rm": delete,
    "cd": change_dir,
    "ls": full_path,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

