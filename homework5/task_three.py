# 1.Создайте программу для игры в ""Крестики-нолики"".
CROSS_SYMBOL = 'x'
ZERO_SYMBOL = '0'


def create_board():
    board = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
    return board


def ask_turn(number_turn):
    if is_cross_turn(number_turn):
        return input("Ходят крестики.Введите координаты ячейки через пробел: ").split(" ")

    else:
        return input("Ходят нолики.Введите координаты ячейки через пробел: ").split(" ")


def update_board(board, coordinate, number_turn):
    symb = ''
    if is_cross_turn(number_turn):
        symb = CROSS_SYMBOL
    else:
        symb = ZERO_SYMBOL

    board[int(coordinate[0])][int(coordinate[1])] = symb


def is_cell_busy(board, coordinate):
    return board[int(coordinate[0])][int(coordinate[1])] == CROSS_SYMBOL \
           or board[int(coordinate[0])][int(coordinate[1])] == ZERO_SYMBOL


def is_cross_turn(number_turn):
    return number_turn % 2 == 0


def print_board(board):
    for i in range(0, len(board)):
        for i2 in range(0, len(board[i])):
            print(board[i][i2], end=' ')
        print()


def is_game_winner(board):
    for i in range(len(board)):
        if board[i][0] == '1':
            break
        if board[i][0] == board[i][1] == board[i][2]:
            return True
    for i in range(len(board[0])):
        if board[0][i] == '1':
            break
        if board[0][i] == board[1][i] == board[2][i]:
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != 1:
        return True
    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != 1:
        return True


if __name__ == "__main__":
    game_board = create_board()
    print_board(game_board)
    turn_number = 1
    while turn_number <= 9:
        coords = ask_turn(turn_number)
        while is_cell_busy(game_board, coords):
            print("Ячейка занята")
            coords = ask_turn(turn_number)
        update_board(game_board, coords, turn_number)
        print_board(game_board)
        if is_game_winner(game_board):
            print(" Вы победили")
            break
        turn_number += 1

    if turn_number > 9:
        print("Ничья")