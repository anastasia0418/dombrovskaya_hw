
__author__ = 'Домбровская Анастасия Петровна'

import random

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonachi (n,m):
    lst = []
    f = 1
    result = 0
    i = 1
    while i <= m:
        f, result = result, f + result
        if i >= n:
            lst.append(result)
        i += 1
    return lst
print(fibonachi(5,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    length = len(origin_list)
    for i in range(length - 1):
        for c in range(length - i - 1):
            if origin_list[c] > origin_list[c + 1]:
                origin_list[c], origin_list[c + 1] = origin_list[c + 1], origin_list[c]
    return origin_list

print (sort_to_max ([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filt(func, list):
    new_list = []
    for i in list:
        if func(i):
            new_list.append(i)
    return  new_list


n = (input('Введите число элементов массива: '))

if n.isdigit():
    lst = []
    for i in range(1, int(n)):
        lst.append(random.randint(-100, 100))
    print(lst)

print(filt(lambda x: x > 4, lst))

# Задача-4:
# Даны четыре точки А(х1, у1), B(x2 ,у2), C(x3 , у3), D(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

x1 = int(input('Введите координату x1 для точки А: '))
y1 = int(input('Введите координату y1 для точки А: '))
x2 = int(input('Введите координату x2 для точки B: '))
y2 = int(input('Введите координату y2 для точки B: '))
x3 = int(input('Введите координату x3 для точки C: '))
y3 = int(input('Введите координату y3 для точки C: '))
x4 = int(input('Введите координату x4 для точки D: '))
y4 = int(input('Введите координату y4 для точки D: '))

if y1 == y4 and y2 == y3 and abs(x1-x2) == abs(x3-x4):
    print('Это параллелограмм')
else:
    print('Это не параллелограмм')
