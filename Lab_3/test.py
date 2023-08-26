import csv
with open("data.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        # Вывод строк
        print(f' {row["Имя"]} - {row["Успеваемость"]}', end='')
        print(f' и он родился в {row["Год рождения"]} году.')
        count += 1
    print(f'Всего в файле {count + 1} строк.')