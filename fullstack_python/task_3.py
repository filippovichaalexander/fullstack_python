# создание 1-го файла
file_name = 'task_3_output.txt'

with open(file_name, 'w', encoding='utf-8') as file:
    print("Введите 6 строк, которые нужно записать в файл:")
    for i in range(3):
        line = input(f"Строка {i+1}: ")

        file.write(line + '\n')

print(f"Строки успешно записаны в файл '{file_name}'.")

# создание 2-го файла
file_name_2 = 'task_3_output_2.txt'

with open(file_name_2, 'w', encoding='utf-8') as file:
    print("Введите 6 строк, которые нужно записать в файл:")
    for i in range(3):
        line = input(f"Строка {i+1}: ")

        file.write(line + '\n')

print(f"Строки успешно записаны в файл '{file_name_2}'.")

# сравнивание файлов
def compare_files(file_name, file_name_2):


    with open(file_name, 'r', encoding='utf-8') as file1, open(file_name_2, 'r', encoding='utf-8') as file2:

        lines1 = file1.readlines()
        lines2 = file2.readlines()

        for i in range(len(lines1)):
            if lines1[i].strip() != lines2[i].strip():
                print(f"Файлы отличаются на строке {i + 1}.")
                print(f"Файл 1: {lines1[i].strip()}")
                print(f"Файл 2: {lines2[i].strip()}")
                return

        print("Все строки совпадают.")

compare_files('task_3_output.txt', 'task_3_output_2.txt')