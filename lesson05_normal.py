
__author__ = 'Домбровская Анастасия Петровна'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from my_lib import *

print("Hello!")
do = ''
while do != 5:
    print('I can do:')
    print('[1] - go to the folder')
    print('[2] - show files in this folder')
    print('[3] - delete the folder')
    print('[4] - create the folder')
    print('[5] - finish work')
    do = int(input('choose the answer: '))
    if do == 1:
        curr_path = input('Which folder do you need? ')
        if os.path.exists(curr_path):
            print('Entered.')
        else:
            print("Such a folder doesn't exist!")
    elif do == 2:
        print('Your files: ', show_files(curr_path))
    elif do == 3:
        path = input('Which folder do you want to delete? ')
        del_dir(path)
    elif do == 4:
        path = input('Which folder do you want to create? ')
        create_dir(path)
    elif do == 5:
        print('Good bye!')
        sys.exit()
        #break
    else:
        print('Unknown answer')

