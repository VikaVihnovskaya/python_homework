# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

if __name__ == "__main__":
    x = int(input('Введите координату х: '))
    y = int(input('Введите координату y: '))
    if x == 0 and y == 0:
        print(' Введите другие числа.Координаты не должны ровняться нулю')
    elif x > 0 and y > 0:
        print('Точка находиться в первой четверти')
    elif x < 0 and y > 0:
        print('Точка находиться во второй четверти')
    elif x < 0 and y < 0:
        print('Точка находиться в третьей четверти')
    elif x > 0 and y < 0:
        print('Точка находиться в четвертой четверти')
