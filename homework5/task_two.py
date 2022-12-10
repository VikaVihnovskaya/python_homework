# 1.Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random

NUMBER_OF_SWEETS = 2021
MAX_CURRENT = 28


def is_gamer_two(number_turn):
    return number_turn % 2 == 0


def choose_turn():
    return random.randint(1, 2)

def ask_turn(number_turn, max_num):
    if is_gamer_two(number_turn):
        return int(input(f"Ходит второй игрок.Введите количество  конфет <= {max_num}: "))

    else:
        return int(input(f"Ходит первый игрок.Введите количество  конфет <= {max_num}: "))


def is_game_winner(current_number_of_sweets, current_value):
    return current_number_of_sweets - current_value == 0



if __name__ == "__main__":

    first_player = 0
    second_player = 0
    turn_number = choose_turn()
    number_of_sweets = NUMBER_OF_SWEETS
    while number_of_sweets > 0:
        value = ask_turn(turn_number, MAX_CURRENT)
        while value > MAX_CURRENT:
            value = ask_turn(turn_number, MAX_CURRENT)
        while value > number_of_sweets:
            value = ask_turn(turn_number, number_of_sweets)
        if is_gamer_two(turn_number):
            second_player += value
        else:
            first_player += value
        if is_game_winner(number_of_sweets, value):
            if is_gamer_two(turn_number):
                second_player += first_player
                first_player = 0
            else:
                first_player += second_player
                second_player = 0
        number_of_sweets -= value
        turn_number += 1
        print(f" Первый игрок забрал {first_player}")
        print(f" Второй игрок забрал {second_player}")
        print(f" Осталось конфет {number_of_sweets}")
    if first_player != 0:
        print("Первый игрок победил")
    else:
        print("Второй игрок победил")