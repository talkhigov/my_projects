board = ['#', ' X ', ' 0 ', ' X ', ' 0 ', ' X ', ' 0 ', ' X ', ' 0 ', ' X ']
boardd = ['   '] * 10
board = ['   '] * 10

def display_board():
    print('\n' * 50) 
    print(boardd[7] + '|' + boardd[8] + '|' + boardd[9])
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(boardd[7] + '|' + boardd[8] + '|' + boardd[9])
    print('-----------')
    print(boardd[7] + '|' + boardd[8] + '|' + boardd[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(boardd[7] + '|' + boardd[8] + '|' + boardd[9])
    print('-----------')
    print(boardd[7] + '|' + boardd[8] + '|' + boardd[9])
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(boardd[1] + '|' + boardd[2] + '|' + boardd[3])

old = [False]  

import random
from time import sleep

def choose_first():
    players = random.randint(1, 2)
    return f'Первым ходит: Игрок {players}'

def player_input():
    marker = None
    while marker != 'X' and marker != '0':
        if old[-1] == False:
            marker = input('Игрок 1, кем Вы хотите играть? X or 0: ').upper()
            if marker == 'X' or marker == '0':
                print(choose_first())     
                sleep(2)
        else:
            break
    return marker

positions = []

def position():
    display_board()
    position = None
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Ваш ход 1-9: '))
            positions.append(position)
        except ValueError:
            print('Введите только число!')
    return position

def place_marker(board, marker, position):
    if old[-1]:
        if old[-1] == 'X':
            marker = '0'
            board[position] = f' {marker} '
            old.append(marker)
        elif old[-1] == '0':
            marker = 'X'
            board[position] = f' {marker} '
            old.append(marker)
    else:
        board[position] = f' {marker} '
        old.append(marker)

def win_check(board): 
    if board[1] == ' X ' and board[2] == ' X ' and board[3] == ' X ' or  board[4] == ' X ' and board[5] == ' X ' and board[6] == ' X ' or board[7] == ' X ' and board[8] == ' X ' and board[9] == ' X ' or board[1] == ' X ' and board[4] == ' X ' and board[7] == ' X ' or board[2] == ' X ' and board[5] == ' X ' and board[8] == ' X ' or board[3] == ' X ' and board[6] == ' X ' and board[9] == ' X ' or board[1] == ' X ' and board[5] == ' X ' and board[9] == ' X ' or board[3] == ' X ' and board[5] == ' X ' and board[7] == ' X ':
        return True
    elif board[1] == ' 0 ' and board[2] == ' 0 ' and board[3] == ' 0 ' or  board[4] == ' 0 ' and board[5] == ' 0 ' and board[6] == ' 0 ' or board[7] == ' 0 ' and board[8] == ' 0 ' and board[9] == ' 0 ' or board[1] == ' 0 ' and board[4] == ' 0 ' and board[7] == ' 0 ' or board[2] == ' 0 ' and board[5] == ' 0 ' and board[8] == ' 0 ' or board[3] == ' 0 ' and board[6] == ' 0 ' and board[9] == ' 0 ' or board[1] == ' 0 ' and board[5] == ' 0 ' and board[9] == ' 0 ' or board[3] == ' 0 ' and board[5] == ' 0 ' and board[7] == ' 0 ':
        return True

def space_check(board, position):
    return board[position] == '   '
    
def full_board_check(board):
    if board[1] != '   ' and board[2] != '   ' and board[3] != '   ' and board[4] != '   ' and board[5] != '   ' and board[6] != '   ' and board[7] != '   ' and board[8] != '   ' and board[9] != '   ':
        return True
    
def replay():
    answer = None
    while answer != 'YES' and answer != 'NO':
        answer = input('Хотите ли вы играть снова? Yes or No: ').upper()
        if answer == 'YES':
            return True

    
print('Добро пожаловать в игру Икс-Нолик!')
while True:       
    place_marker(board, player_input(), position())
    if win_check(board):
        display_board()
        print('ВЫ ВЫИГРАЛИ!!!')
        if replay():
            for i in range(1, 10):
                board[i] = '   '
            place_marker(board, player_input(), position())
        else:
            break
    elif full_board_check(board):
        display_board()
        print('НИЧЬЯ!')
        if replay():
            for i in range(1, 10):
                board[i] = '   '
            place_marker(board, player_input(), position())
        else:
            break