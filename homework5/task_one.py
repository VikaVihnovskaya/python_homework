# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# str_Text = 'Я хочу классно иабв продуктивноабв кодить на Джавеабв иабв Питоне'
# lst = str_Text.split(' ')
# print(lst)
# my_list = []
# for i in lst:
#     if 'абв' not in i:
#         my_list.append(i)
# print(*my_list)
with open("task_1.txt", "r+") as data:
    str_Text = data.readline()
    print(str_Text)
    data.write(' '.join([i for i in str_Text.split(' ') if 'абв' not in i]))
    print(' '.join([i for i in str_Text.split(' ') if 'абв' not in i]))




