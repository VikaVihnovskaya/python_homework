# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 10.01] => 0.19



if __name__ == "__main__":
    numbers = input('Введите  список вещественных чисел через пробел: ').split(' ')
    new_list = []
    min_num = float(numbers[0]) * 100 % 100
    max_num = float(numbers[0]) * 100 % 100
    for i in range(0, len(numbers)):
        current = float(numbers[i]) * 100 % 100
        if current < min_num:
            min_num = current
        elif current > max_num:
            max_num = current
    result = float(max_num - min_num) / 100
    print(result)


