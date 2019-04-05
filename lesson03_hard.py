
__author__ = 'Домбровская Анастасия Петровна'

import os
from collections import defaultdict
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def space(numb, slash):
    if ' ' in numb:
        space = numb.find(' ')
        n1 = numb[:space]
        x1 = numb[space + 1:]
    else:
        n1 = 0
        x1 = numb[:slash]
    return int(n1), int(x1)


def findYNX (tofind, numb, slash2):
    sing = numb.find(tofind)
    y1 = numb[:sing]
    numb2 = numb[sing + 1:slash2].strip()
    y2 = numb[slash2 + 1:]
    n2, x2 = space(numb2, slash2)
    return int(y1), int(y2), int(n2), int(x2)


equation1 = input("Введите пример: ")
slash1 = equation1.find('/')
numb = equation1[:slash1].strip()
n1, x1 = space(numb, slash1)
numb1 = equation1[slash1+1:]
slash2 = numb1.find('/')

if '+' in numb1:
    y1, y2, n2, x2 = findYNX('+', numb1, slash2)
elif '-' in numb1:
    y1, y2, n2, x2 = findYNX('-', numb1, slash2)

if y1 == y2:
    resultN = n1+n2
    resultX = x1+x2
    resultY = y1
    if resultX >= y1:
        resultN += 1
        resultX -= y1
else:
    x1 = n1*y1+x1
    x2 = n2*y2+x2
    resultY = y1*y2
    resultN = int(((x1*y2) + (x2*y1)) / resultY)
    resultX = ((x1*y2) + (x2*y1)) - resultY*resultN

if resultY % resultX == 0:
    resultY = int(resultY / resultX)
    resultX = int(resultX/resultX)

print(resultN, resultX, '/', resultY)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def createDict (path):
    f = open(path, 'r', encoding='UTF-8-sig')
    dic = {}
    for line in f:
        line = line.split()
        dic[line[0]] = int(line[1])
    f.close()
    return dic


dicOtr = createDict(path=os.path.join('hours_of_work.txt'))
dicOklad = createDict(path = os.path.join('workers.txt'))

norma = int(100)  # норма часов
moneyInHour = {}
for key, value in dicOklad.items():
    money = value/norma
    moneyInHour[key] = money


for key, value in dicOtr.items():
    if norma == value:
        print(key, dicOklad.get(key))
    elif value < norma:
        print(key, moneyInHour.get(key)*value)
    else:
        print(key, (dicOklad.get(key)) + (value - norma)*moneyInHour.get(key)*2)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

allfr = {}
with open('fruits.txt', 'r', encoding='UTF-8-sig') as file:
    for line in file:
        for word in line.split():
            if not word:
                continue
            word = word.lower()
            if word[0] not in allfr:
                allfr[word[0]] = list()
            allfr[word[0]].append(word)
for key in allfr:
    allfr[key] = list(allfr[key])
print(allfr)

for key, value in allfr.items():
    with open('fruits_' + key + '.txt', 'w', encoding='UTF-8-sig') as newfr:
        newfr.write('\n'.join(value))

