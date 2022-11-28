# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0

n = int(input('Введите число: '))
new_list = []
for i in range( -n, n + 1):
    new_list.append(i)
print(new_list, end=' ')
indexes = input(' Введите индексы через пробел: ').split(' ')
mult = 1
for i in indexes:
    k = int(i)
    if int(k) < 0 or k > len(new_list)-1:
        continue
    mult = mult * new_list[k]

print(mult)




