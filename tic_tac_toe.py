import random


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


board = list(range(1, 10))
display_board(board)


def winner(answer):
    combinations_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in combinations_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] == answer:
            return True
    return False


while True:
    answer = input('Выбирай: (X/O)')
    answer.islower
    if answer == 'x':
        print('Ладно, ходи первым =/')
        comp_answer = 'o'
        break
    elif answer == 'o':
        print('Тогда жди, первым хожу я =)')
        comp_answer = 'x'
        break
    else:
        print('Ты что-то напутал. Такого варианта нет.')


def player_move():
    while True:
        player_move = int(input('Твой ход\nКуда хочешь поставить? '))
        if board[player_move - 1] == 'x' or board[player_move - 1] == 'o':
            print('Посмотри-ка внимательнее... Видишь? Это поле уже занято!')
        else:
            board[player_move - 1] = answer
            display_board(board)
            break
    return winner(answer)


def comp_move():
    print('Мой ход')
    while True:
        comp_move = random.randint(1, 9)
        if board[comp_move - 1] != 'x' and board[comp_move - 1] != 'o':
            board[comp_move - 1] = comp_answer
            display_board(board)
            break
    return winner(comp_answer)


count = 0
win = ''
while count <= 9:
    if comp_answer == 'x':
        if comp_move():
            count += 1
            win = 'Я'
            break
        count += 1
        if count == 9:
            break
        if player_move():
            count += 1
            win = 'Ты'
            break
        count += 1
    else:
        if player_move():
            count += 1
            win = 'Ты'
            break
        count += 1
        if count == 9:
            break
        if comp_move():
            count += 1
            win = 'Я'
            break
        count += 1

if win == '':
    print('Ничья')
else:
    print(win, ' выйграл!')
