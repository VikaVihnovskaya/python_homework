# Вычислить число c заданной точностью d
#
# Пример:
#
# - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14
#
#     Ввод: 0.001
#     Вывод: 3.141
import math


if __name__ == "__main__":
    d = str(input('Введите точность, с которой хотите вывести число пи: '))
    pi = str(math.pi)
    formatted_pi = pi[0:len(d)]
    print(formatted_pi)

