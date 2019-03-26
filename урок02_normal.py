
__author__ = 'Домбровская Анастасия Петровна'

import math
import random
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru')
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print('Задача №1.')
numbers = [2, -5, 8, 9, -25, 25, 4]
array = []
for i in numbers:
    if abs(i) == i:
        newNumbers = math.sqrt(i)
        if newNumbers.is_integer():
            array.append(int(newNumbers))
print(array)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('Задача №2.')
day_list = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
date_list = datetime.date.today().strftime("%x").split('.')
print(day_list[int(date_list[0])-1] + ' ' + month_list[int(date_list[1]) - 1] + ' ' + date_list[2] + ' года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('Задача №3.')
n = int(input('Введите целое число: '))
list1 = []
while len(list1) < n:
    number = random.randint(-100, 100)
    list1.append(number)
print(list1)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print('Задача №4.')
lst = [1, 2, 4, 5, 6, 2, 5, 2]
print(f'Изначальный список {lst}')
newLst = list(set(lst))
print(f'Неповторяющиеся элементы исходного списка: {newLst}')

newLst = []
for i in lst:
    if lst.count(i) == 1:
        newLst.append(i)
print(f'Элементы, которые не имеют повторений: {newLst}')

# OR
"""
for i in lst:
    if i not in newLst:
        newLst.append(i)
print(f'Неповторяющиеся элементы исходного списка: {newLst}')

d = {}
for i in lst:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1
newLst = []
for key, value in d.items():
    if value == 1:
        newLst.append(key)
print(f'Элементы, которые не имеют повторений: {newLst}')
"""

