import random


def check_n():  # Метод для считывания размера списка
    i = 0
    while i < 1:  # Цикл для ввода и обработки на корректность
        try:
            x: int = int(input("Enter list size: "))
            i = 1
        except ValueError:  # Обработка ошибки
            print("Enter only a number!")
    return x  # Возвращает размер списка


def mode_selection(size):  # Метод для выбора ввода
    i = 0
    numlist = []  # Создания списка
    while i != 1:  # Цикл для ввода и обработки на корректность
        try:
            # принимается число от пользователя
            x = int(input("Enter '0' for keyboard input or '1' for random generation: "))
            # Если 0, то ввод с клавиатуры
            if x == 0:
                numlist = enter_list(size)
                i = 1
            # Если 1, то список генерируется автоматический
            elif x == 1:
                numlist = random_list(size)
                i = 1
            else:
                print("Enter only '0' or '1'!")
        except ValueError:  # Обработка ошибки
            print("Enter only a number!")
    print("Your list:", numlist)
    return numlist  # Возвращает список


def enter_list(size):  # Метод для ввода списка и обработки корректности ввода
    i = 0
    numlist = []  # Создания списка
    while i < size:  # Цикл для заполнения списка и обработки на корректность
        string = "Enter number #" + str(i + 1) + ": "
        try:
            x = int(input(string))
            numlist.append(int(x))
            i += 1
        except ValueError:  # Обработка ошибки
            print("Enter an integer!")
    return numlist  # Возвращает список


def random_list(size):  # Метод для генерации рандомных чисел
    numlist = []  # Создания списка
    for num in range(size):  # Цикл для генерации рандомных чисел
        numlist.append(random.randint(0, 10))  # Добавления рандомных чисел в список
    return numlist  # Возвращает список


def selection_sort(size, alist):  # Метод для сортировки выбором
    for i in range(0, size - 1):  # Внешний цикл
        min_x = i  # Переменная для мин элемента
        for j in range(i + 1, size):  # Внутренний цикл для обхода списка
            if alist[j] < alist[min_x]:  # Если j меньше min_x то
                min_x = j  # присваиваем min_x значения j
        alist[i], alist[min_x] = alist[min_x], alist[i]  # Меняем местами макс и мин
    print("Your sorted list:", alist)


n = check_n()
num_list = mode_selection(n)
num_list.sort()
print(num_list)
