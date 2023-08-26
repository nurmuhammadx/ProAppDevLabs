
from pathlib import Path

def count_files():  # метод для подсчета колво файлов в директории
    k = 0
    path = str(input('Enter path: '))
    for item in Path(path).glob('*'):
        if item.is_file():
            # print(str(item))
            k += 1
    print('The number of files in this directory:', k)


import csv


# Считываем данные из CSV файла в словарь
def read_csv_to_dict(mdict):
    with open('data.csv', 'r', encoding='cp1251') as r_file:
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
    print('Исходные данные:')


# Сохранение данных в файл
def write_dict_to_csv(mdict):
    with open('new_data.csv', 'w', newline='') as w_file:
        file_writer = csv.writer(w_file)

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

    print('\nСохранение данных в файл: new_data.csv')


# new_call_info = {
#     'phone': '555-5555',
#     'picked_up': False,
#     'fio': 'Иванов Иван',
#     'next_call_date': '2022-01-01',
#     'next_step': 'Позвонить позже'
# }
# data_dict[new_call_id] = new_call_info



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
        print(mydict)
    else:
        print("Enter only '0' or '1'!")
        choose_mode()




if __name__ == "__main__":
    mydict = {}
    choose_mode()

    # write_dict_to_csv(mydict)


# import os.path
# path = "/mnt/c/users/end/pictures/wallpaper"
# num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
# print(num_files)