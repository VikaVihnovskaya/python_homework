# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not

def get_bool_value(param_name):
    bool_value = input("Введите значение для {}: True/False ".format(param_name))
    if bool_value == "True":
        return True
    if bool_value == "False":
        return False


if __name__ == "__main__":
    x = get_bool_value("x")
    y = get_bool_value("y")
    z = get_bool_value("z")
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    if result:
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')
