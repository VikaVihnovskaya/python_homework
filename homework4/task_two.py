# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

if __name__ == "__main__":
    n = int(input('Введите число N: '))
    numbers_list = []
    for i in range(1, n + 1):
        if i <= 3:
            numbers_list.append(i)
            continue
        if i % 2 == 0 or i % 3 == 0:
            continue
        numbers_list.append(i)
    print(numbers_list)



