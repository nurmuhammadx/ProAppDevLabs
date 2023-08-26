from pathlib import Path
import csv


def count_files():  # метод для подсчета колво файлов в директории
    k = 0
    path = str(input('Enter path: '))
    for item in Path(path).glob('*'):
        if item.is_file():
            # print(str(item))
            k += 1
    print('The number of files in this directory:', k)


# Считываем данные из CSV файла в словарь
def read_csv_to_dict(mdict):

    """
    Ошибка UnicodeDecodeError возникает, когда встречается символ, который невозможно декодировать в кодировку UTF-8.
    Для решения этой ошибки можно указать правильную кодировку при чтении CSV файла.
    Попробуйте использовать кодировку "cp1251" (Windows-1251), которая часто используется для файлов CSV, содержащих русские символы.
    """
    # Использовать encoding='cp1251', если возникает ошибка UnicodeDecodeError
    with open('data.csv', 'r') as r_file: #
        file_reader = csv.reader(r_file, delimiter=';')

        # Пропускаем заголовок
        header = next(file_reader)

        for row in file_reader:
            call_id = row[0]
            phone = row[1]
            picked_up = row[2]
            fio = row[3]
            next_call_date = row[4]
            next_step = row[5]

            mdict[call_id] = {
                'phone': phone,
                'picked_up': picked_up,
                'fio': fio,
                'next_call_date': next_call_date,
                'next_step': next_step

            }

    print('Initial data:')
    for key, value in mdict.items():
        print(key, '=>', value)


# Сохранение данных в файл
def write_dict_to_csv(mdict):
    with open('data.csv', 'w', newline='') as w_file:
        file_writer = csv.writer(w_file, delimiter=';')

        # Записываем заголовок
        file_writer.writerow(['№', 'телефон', 'взял трубку или нет', 'ФИО клиента', 'дата следующего созвона',
                              'описание следующего шага для обзвона'])

        # Записываем данные
        for call_id, call_info in mdict.items():
            phone = call_info['phone']
            picked_up = call_info['picked_up']
            fio = call_info['fio']
            next_call_date = call_info['next_call_date']
            next_step = call_info['next_step']

            file_writer.writerow([call_id, phone, picked_up, fio, next_call_date, next_step])

    print('\nSaving data to a file: new_data.csv')


# Добавление новых данных в файл
def add_new_user(mdict):
    new_call_id = int(input('Enter a new call ID: '))
    phone = input("Enter client's phone number: ")
    picked_up = input('Picked up the phone or not: ')
    fio = input("Client's full name: ")
    next_call_date = input('Date of the next call: ')
    next_step = input('Description of the next step for calling: ')

    new_call_info = {
        'phone': phone,
        'picked_up': picked_up,
        'fio': fio,
        'next_call_date': next_call_date,
        'next_step': next_step
    }

    mdict[new_call_id] = new_call_info
    print('\nUpdated data:')
    for key, value in mdict.items():
        print(key, '=>', value)


# Сортировка по полю ФИО клиента (строковому)
def sort_by_string_field(mdict, field):
    sorted_dict = {}

    sorted_keys = sorted(mdict.keys(), key=lambda x: mdict[x][field])

    for key in sorted_keys:
        sorted_dict[key] = mdict[key]

    print("\nSorting by the client's full name field (string)")
    for key, value in sorted_dict.items():
        print(key, '=>', value)


# Сортировка по номеру тел
def sort_by_numeric_field(mdict, field):
    sorted_dict = {}

    sorted_keys = sorted(mdict.keys(), key=lambda x: int(mdict[x][field]))

    for key in sorted_keys:
        sorted_dict[key] = mdict[key]

    print('\nSorting by phone number:')
    for key, value in sorted_dict.items():
        print(key, '=>', value)


# Фильтрация по полю "взял трубку или нет"
def filter_by_criteria(data_dict, field, value):
    filtered_dict = {}

    for key, call_info in data_dict.items():
        if field in call_info and call_info[field] == value:
            filtered_dict[key] = call_info

    print('\nFiltering by the field "picked up the phone or not":')
    for key, value in filtered_dict.items():
        print(key, '=>', value)


def check_n():  # метод для обрабоки ввода
    i = 0
    while i < 1:
        try:
            print("\nEnter from 0 to 5 to select an option:\n1) Sorting by the client's full name field (string)\n"
                  "2) Sorting by phone number\n3) Filtering by the field 'picked up the phone or not'\n"
                  "4) Add a new user\n5) Save to a new .csv file\n0) Exit\n")
            n: int = int(
                input('Enter: '))
            i = 1
        except ValueError:  # Обработка ошибки
            print("Enter only a number!")
    return n


def choose_mode_filter():

    while True:
        num_x = check_n()
        if num_x == 1:
            sort_by_string_field(mydict, 'fio')
        elif num_x == 2:
            sort_by_numeric_field(mydict, 'phone')
        elif num_x == 3:
            filter_by_criteria(mydict, 'picked_up', 'Да')
        elif num_x == 4:
            add_new_user(mydict)
        elif num_x == 5:
            write_dict_to_csv(mydict)
        elif num_x == 0:
            break
        else:
            print("Enter only '0' to '5'!")
            choose_mode_filter()


def check_x():  # метод для обрабоки ввода
    i = 0
    while i < 1:
        try:
            x: int = int(
                input('Enter 1 to count the number of files in the directory or 2 to process the ".csv" file: '))
            i = 1
        except ValueError:  # Обработка ошибки
            print("Enter only a number!")
    return x


def choose_mode():
    num_x = check_x()
    if num_x == 1:
        count_files()
    elif num_x == 2:
        read_csv_to_dict(mydict)
        choose_mode_filter()
    else:
        print("Enter only '1' or '2'!")
        choose_mode()


if __name__ == "__main__":
    mydict = {}
    choose_mode()