from data_base import write_contact, rewrite
from funcs import search, delete_contact, import_file, correction_data, data_to_list, print_tabl_numbook


def redactor():
    while True:
        print('\n\t\t*****Главное Меню*****')
        print('''
              1 - Редактировать Данные
              2 - Добавить
              3 - Удалить
              4 - Поиск
              5 - Вывести список
              6 - Импорт
              7 - Выход
              ''')
        str_in = input()
        if str_in == "1":
            print('')
            rewrite(correction_data(data_to_list()))
            return redactor()
        elif str_in == "2":
            write_contact()
        elif str_in == "3":
            rewrite(delete_contact(data_to_list()))
        elif str_in == "4":
            search(data_to_list())
        elif str_in == "5":
            print_tabl_numbook()
        elif str_in == "6":
            text = input('Введите путь к файлу: ')
            rewrite(import_file(text))
        elif str_in == "7":
            break