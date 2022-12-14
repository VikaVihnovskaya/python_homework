# 1 Реализуйте алгоритм перемешивания списка
# import random
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = sorted(my_list, key=lambda x: random.random())
# print(new_list)



# 2 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# filtered_list = list(filter(lambda i: i % 2 != 0, my_list))
# print(filtered_list)
# print(sum(filtered_list))


# 3 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from math import factorial

num = int(input('Введите число: '))
mult = lambda x: ((x == 1) and 1) or x * factorial(x -1)
new_list = list(mult(i) for i in range(1, num +1))
print(new_list)

