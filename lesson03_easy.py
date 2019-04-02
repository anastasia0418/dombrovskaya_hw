
__author__ = 'Домбровская Анастасия Петровна'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = str(number)
    if number.find('.') is None:
        print(number)
        return
    stop = number.find('.')
    start = number.find('.')+1
    numb = int(number[:stop])
    mark = (number[start:])
    if len(mark) <= ndigits:
        print(number)
        return
    if ndigits == 0:
        okr = int(mark[0])
        if okr > 5:
            numb = numb + 1
            print(numb)
        else:
            print(numb)
    elif len(mark) > 0:
        okr = int(mark[ndigits])
        okr2 = int(mark[:ndigits])
        if okr > 5:
            okr2 = okr2 + 1
            while okr2 % 10 == 0:
                okr2 = int(okr2 / 10)
            print(f'{numb}.{okr2}')
        else:
            print(f'{numb}.{okr2}')


my_round(2.1234567, 5)
my_round(2.1999967, 5)
my_round(2.9999967, 5)
my_round(2.9999967, 0)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    first3 = list(ticket_number[:3])
    first3 = [int(i) for i in first3]
    last3 = list(ticket_number[-3:])
    last3 = [int(i) for i in last3]
    sumFirst = sum(first3)
    sumLast = sum(last3)
    if len(ticket_number) != 6:
        result = 'Это не шестизначный номер!'
    elif sumFirst == sumLast:
        result = 'Счастливый билет! =)'
    else:
        result = 'Несчастливый билет! =('
    return result

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

