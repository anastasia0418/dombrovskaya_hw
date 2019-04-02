
__author__ = 'Домбровская Анастасия Петровна'

# Все задачи текущего блока решите с помощью генераторов списков!
import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print('Задание-1\n')
lstGenerate = [random.randint(0, 100) for _ in range(5)]
print('Сгенерированный список: ', lstGenerate)
newList = [i**2 for i in lstGenerate]
#for i in lstGenerate:
   # i = i**2
   # newList.append(i)
print('Список возведенный в квадрат ', newList)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print('\nЗадание-2\n')
fruits = ['яблоко', 'киви', 'банан', 'манго', 'груша', 'ананас', 'дыня', 'апельсин', 'мандарин']
newFruits1 = [fruits[random.randint(0, len(fruits)-1)] for i in range(5)]
newFruits2 = [fruits[random.randint(0, len(fruits)-1)] for i in range(9)]
print('Список 1: ', newFruits1)
print('Список 2: ', newFruits2)
newFruits = [el for el in newFruits2 if el in newFruits1]
print('Отсортированный список: ', newFruits)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print('\nЗадание-3\n')
lstGen = [random.randint(-100, 100) for _ in range(30)]
print('Сгенерированный список: ', lstGen)
newList = [el for el in lstGen if el % 3 == 0 and el % 4 != 0 and el >= 0]
print('Отсортированный список: ', newList)
