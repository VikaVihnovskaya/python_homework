# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и
if __name__ == "__main__":
    number = int(input('Введите номер четверти: '))
    if number == 1:
        print('Координаты возможных точек x > 0 and y > 0')
    elif number == 2:
        print('Координаты возможных точек x < 0 and y > 0')
    elif number == 3:
        print('Координаты возможных точек x < 0 and y < 0')
    elif number == 4:
        print('Координаты возможных точек x > 0 and y > 0')
    else:
        print('Это число не подходит. Введите другое число от 1 до 4')

