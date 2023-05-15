from pathlib import Path


def count_files():  # метод для подсчета колво файлов в директории
    k = 0
    path = str(input('Enter path: '))
    for item in Path(path).glob('*'):
        if item.is_file():
            # print(str(item))
            k += 1
    print('The number of files in this directory: ', k)


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
        print('hello world')
    else:
        print("Enter only '0' or '1'!")
        choose_mode()


if __name__ == '__main__':
    choose_mode()
