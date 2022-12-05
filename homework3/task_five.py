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
# def feb(num):
# list = [0, 1, 1]
# list_1 = []
# for i in range(1, num-1):
# list.append(list[i]+list[i+1])
# for i in range(1, len(list)):
# list_1.append(list[-i])
# i = -2
# while i >= (len(list_1) * (-1)):
# list_1[i] *= (-1)
# i -= 2
# total = list_1 + list
# return total
#
# num = int(input('Введите число: '))
# print(feb(num)
# def fibonacci(n):
# if n in (1, 2):
# return 1
# return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# def reversed_fibonacci(n):
# if n in (1, 2):
# return 1
# return reversed_fibonacci(n + 2) - reversed_fibonacci(n + 1)
#
#
# def negafibonacci() -> list:
# a = []
# b = []
# try:
# n = int(input("Введите число для последовательности Фибоначчи:"))
# if type(n) in [int]:
# for i in range(-n, n + 1):
# if i > 0:
# a.append((fibonacci(i)))
# else:
# b.append(reversed_fibonacci(i))
# return f'- для k={n} список будет выглядеть так: {b + a}'
# except ValueError as e:
# print(e)
# return negafibonacci()
#
#
# print(negafibonacci())