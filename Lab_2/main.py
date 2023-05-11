import numpy as np


def check_n():  # Метод для считывания размера списка
    i = 0
    while i < 1:  # Цикл для ввода и обработки на корректность
        try:
            x: int = int(input("Enter row size: "))
            i = 1
        except ValueError:  # Обработка ошибки
            print("Enter only a number!")
    return x  # Возвращает размер списка


def check_m():  # Метод для считывания размера списка
    i = 0
    while i < 1:  # Цикл для ввода и обработки на корректность
        try:
            x: int = int(input("Enter column size: "))
            i = 1
        except ValueError:  # Обработка ошибки
            print("Enter only a number!")
    return x  # Возвращает размер списка


def column_elements(row, column, arr):
    column_list = []  # список для хранения колво нулевых элементов
    for j in range(column):
        k = 0
        for i in range(row):
            if arr[i][j] == 0:
                k += 1
        column_list.append(k)  # добавления элементов
    arr_column = np.asarray(column_list).reshape((1, -1))  # конверт list to array и изменения формы массива
    return np.concatenate([arr, arr_column], axis=0)  # добавления колво нулевых элем в основной массив


def row_elements(row, column, arr):
    row_list = []  # список для хранения колво нулевых элементов
    for i in range(row):
        k = 0
        for j in range(column):
            if arr[i][j] == 0:
                k += 1
        row_list.append(k)  # добавления элементов
    arr_row = np.asarray(row_list).reshape((-1, 1))  # конверт list to array и изменения формы массива
    return np.concatenate([arr, arr_row], axis=1)  # добавления колво нулевых элем в основной массив


def save_result(arr1, arr2):
    file = open('output.txt', 'w')
    file.write("Source array: \n" + np.array_str(arr1) + "\n\nArray after processing: \n" + np.array_str(arr2))
    file.close()
    print("\nThe array has been processed! The result is saved in a file 'output.txt'.")


if __name__ == "__main__":  # вызов всех функций
    n = check_n()
    m = check_m()
    mass = np.random.randint(0, 2, size=(n, m))  # создания двумерного массива с автозаполнением
    new_mass = column_elements(n, m, mass)
    result = row_elements(n + 1, m, new_mass)
    save_result(mass, result)
