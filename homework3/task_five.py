# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibo(n):
    if n >= 0:
        index = range(n + 1)
        result = [0, 1]
        for k in index[2:]:
            result.append(result[k - 1] + result[k - 2])
        return result[n]
    else:
        n = -(n - 1)
        index = range(n + 1)
        result = [1, 0]
        for k in index[2:]:
            result.append(result[k - 2] - result[k - 1])
        result.reverse()
    return result[0]


if __name__ == "__main__":
    n = int(input('Введите число '))
    list = []
    for i in range(-n, n + 1):
        list.append(fibo(i))

    print(list)
