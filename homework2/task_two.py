# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
i = 1
mult = 1
while i <= n:
    mult = mult * i
    i += 1
    print([mult], end=' ')




