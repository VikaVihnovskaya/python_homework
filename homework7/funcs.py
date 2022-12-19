from data_base import read_contact
from prettytable import PrettyTable
import logging

file_log = logging.FileHandler("logs.log")
# и вывод в консоль
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), level=logging.INFO)

def data_to_list():
    return read_contact()


def search(data_list: list):
    my_list = []
    find_contact = input('Data for search: ')
    for i in range(len(data_list)):
        if find_contact.lower() in data_list[i]['Name'].lower() or \
                find_contact.lower() in data_list[i]['Surname'].lower() or \
                find_contact.lower() in data_list[i]['Number'].lower():
            my_list.append(data_list[i])
    print_table(my_list)

def delete_contact(data_list: list):
    contact = input('Enter contact surname for deleting: ')
    dict_for_search = {}
    for i in range(len(data_list)):
        if contact in data_list[i]['Surname']:
            dict_for_search[i] = data_list[i]
    if not dict_for_search:
        print("Contact with passed surname isn't found")
        logging.warning(f"Contact with passed surname {contact} isn't found",)
        return data_list

    print(dict_for_search)
    while len(dict_for_search) != 1:
        phone_number = input('Enter number of contact for deleting: ')
        dict_for_search = dict(filter(lambda value: value[1]["Number"] == phone_number, dict_for_search.items()))

    key = list(dict_for_search.keys())[0]
    data_list.remove(dict(dict_for_search[key]))
    return data_list


def correction_data(data_list: list):
    data_for_search = input('Enter surname: ')
    dict_for_search = {}
    for i in range(len(data_list)):
        if data_for_search in data_list[i]['Surname']:
            dict_for_search[i] = data_list[i]
    print(dict_for_search)
    if not dict_for_search:
        print("Contact with passed surname isn't found")
        logging.warning(f"Contact with passed surname {data_for_search} isn't found")
        return data_list
    while len(dict_for_search) != 1:
        phone_number = input('Enter number of contact for change: ')
        dict_for_search = dict(filter(lambda value: value[1]["Number"] == phone_number, dict_for_search.items()))

    print('What do you want to change?')
    list_of_command = ['Name', 'Surname', 'Number']
    while (command := input('Name, Surname or Number')) not in list_of_command:
        print('Wrong command!')
    else:
        data_list[list(dict_for_search.keys())[0]][command] = input('Enter correct data: ')
    return data_list


def import_file(file_name):
    with open(file_name, 'r') as data:
        str_data = data.read()
    str_first_data = read_contact()
    new_list_of_contact = []
    list_of_contact = (str_first_data + str_data).split('\n\n')
    list_of_contact = set(list_of_contact)
    list_of_contact = list(list_of_contact)
    for i in list_of_contact:
        new_list_of_contact.append(i.split('\n'))
    new_list_of_contact.append([''])
    return new_list_of_contact


def conclusion_contact():
    with open('dataBase.txt', 'r') as data:
        print('======================')
        return print(data.read())


def print_tabl_numbook():
    mylist = data_to_list()
    print_table(mylist)


def print_table(list_of_numbers):
    my_table = PrettyTable(["Name", "Surname", "Number"])
    for i in range(len(list_of_numbers)):
        my_table.add_row(list_of_numbers[i].values())
    print(my_table)
