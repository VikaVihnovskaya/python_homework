# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input('Введите число: ')
suma = 0
for digit in n:
    if digit.isdigit():
       suma += int(digit)
# while n > 0:
#      digit = n % 10
#      if digit != 0:
#          suma = suma + digit
#      n = n // 10
print('Сумма равна : ', suma)


