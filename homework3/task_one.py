# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
#
# Пример:
#
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def find_sum(source_list):
    sum = 0
    for i in range(len(source_list)):
        if i % 2 != 0:
           sum = sum + source_list[i]
    return sum


if __name__ == "__main__":
    n = int(input('Введите размер списка: '))
    new_list = []
    for i in range(0, n + 1 ):
        new_list.append(i)
    print(new_list)
    print(find_sum(new_list))

