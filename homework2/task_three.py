# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
import math
n = int(input('Введите число'))
sequence = []
for i in range(1, n+1):
    sequence.append(round(math.pow(1 + 1/i, i), 2))
print(sequence, end=' ')
print('Сумма: ', sum(sequence))






