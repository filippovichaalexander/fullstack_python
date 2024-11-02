import os

file_path = './text.py'


def read_file(file_path):
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return lines


def print_file_contents(file_path):
    lines = read_file(file_path)

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


print_file_contents(file_path)