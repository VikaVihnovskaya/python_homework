import csv

def write_contact():
    with open('dataBase.csv', 'a') as data:
        name = input('Fill a name: ')
        surname = input('Fill a surname: ')
        number = input('Fill a telephone number: ')
        writer = csv.DictWriter(data, ['Name', 'Surname', 'Number'])
        row = {'Name': name, 'Surname': surname, 'Number': number}
        writer.writerow(row)


def read_contact():
    with open('dataBase.csv', 'r') as data:
        reader = csv.DictReader(data)
        return list(reader)


def rewrite(data_list):
    with open('dataBase.csv', 'w') as data:
        writer = csv.DictWriter(data, ['Name', 'Surname', 'Number'])
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)


