# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

if __name__ == "__main__":
    numbers = input('Введите  последовательность чисел через пробел: ').split(' ')
    my_dict = {}
    for i in numbers:
        if i in my_dict:
            my_dict[i] = my_dict[i] + 1
        else:
            my_dict[i] = 1
    new_list = []
    for i in my_dict:
        if my_dict[i] == 1:
            new_list.append(int(i))
    print(new_list)











