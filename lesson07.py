#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random

class Card:

    def __init__(self, name):
        lst = []
        self.card = [__class__.create_line(lst) for _ in range(3)]
        self.name = name
        self.count = 15

    def create_line(lst):
        nums2 = []
        while len(nums2) < 5:
            number = random.randint(1, 90)
            if number not in lst:
                nums2.append(number)
                lst.append(number)
        nums2.sort()
        count = 0
        while count != 4:
            index = random.randint(0, 5+count)
            nums2.insert(index, '')
            count += 1
        return nums2

    def __str__(self):
        presentation = '{:-^26}\n'.format(self.name)
        for i in self.card:
            presentation += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*i) + '\n'
        return presentation + '--------------------------'

def check(i,card):
    isfind = False
    for j in card:
        if i in j:
            j[j.index(i)] = '-'
            isfind = True
    return isfind

card_player = Card('Player')
card_computer = Card('Computer')
barrels = list(range(1, 91))
random.shuffle(barrels)
counter = 89
for i in barrels:
    print(card_player)
    print(card_computer)
    print('New barrel:', str(i), '(', counter, 'left)')
    answer = input('Cross the number? (y/n/q)')
    answer.islower()
    if answer == 'y':
        if check(i, card_player.card) is False:
            print(card_player.name, ' lose!')
            break
        else:
            card_player.count -= 1
        if check(i, card_computer.card) is True:
            card_computer.count -= 1

        if card_player.count == 0 and card_computer.count == 0:
            print('Both win')
            break
        elif card_computer.count == 0:
            print(card_computer.name, ' win!')
            break
        elif card_player.count == 0:
            print(card_player.name, ' win!')
            break
    elif answer == 'n':
        if check(i, card_player.card) is True:
            print(card_player.name, ' lose!')
            break
        if check(i, card_computer.card) is True:
            card_computer.count -= 1
        if card_computer.count == 0:
            print(card_computer.name, ' win!')
            break
    elif answer == 'q':
        print('Good buy!')
        break
    counter -= 1
