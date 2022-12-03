# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def find_mult(source_list):
    mult = []
    j = len(source_list) - 1
    for i in range(len(source_list)):
        if j < i:
            break
        mult.append(source_list[i] * source_list[j])
        j -= 1
    return mult


if __name__ == "__main__":
    n = int(input('Введите размер списка: '))
    new_list = []
    for i in range(1, n + 1):
        new_list.append(i)
    print(new_list)
    print(find_mult(new_list))

