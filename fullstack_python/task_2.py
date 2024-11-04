import os

FILE_PATH = './text.py'


def read_file(FILE_PATH):


    # Проверяем, существует ли файл
    if not os.path.exists(FILE_PATH):
        print(f"Файл {FILE_PATH} не найден.")
        return []

    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return lines


def print_file_contents(FILE_PATH):


    lines = read_file(FILE_PATH)

    if lines:
        # первая строка
        if len(lines) > 0:
            print("Первая строка:", lines[0].strip())

        # пятая строка
        if len(lines) > 4:
            print("Пятая строка:", lines[4].strip())

        # первые 5 строк
        print("Первые 5 строк:")
        for line in lines[:5]:
            print(line.strip())

        # строки с s1-й по s2-ю
        s1 = 1
        s2 = len(lines)
        print(f"Строки с {s1}-й по {s2}-ю:")
        for line in lines[s1 - 1:s2]:
            print(line.strip())

        # e) весь файл
        print("Содержимое всего файла:")
        for line in lines:
            print(line.strip())


print_file_contents(FILE_PATH)