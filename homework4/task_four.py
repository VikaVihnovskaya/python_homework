# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random


def find_term(n):
    random_value = random.randint(0, 100)
    if n == 1:
        return f'{random_value}*x'
    if n == 0:
        return f'{random_value}'

    return f'{random_value}*(x**{n})'

if __name__ == "__main__":
    k = int(input('Введите  натуральную степень: '))
    polynomial = ''
    for i in range(k, -1, -1):
        polynomial = polynomial + find_term(i)
        if i != 0:
            polynomial = polynomial + ' + '
        else:
            polynomial = polynomial + ' = 0'
    print(polynomial)
    with open('file.txt', 'w') as data:
        data.write(polynomial)













