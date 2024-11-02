# task 1
'''
1.Работа с модулем os
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
• Вывести имя вашей ОС
• Вывести путь до папки, в которой вы находитесь
• Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются все
файлы с расширением .txt, то же самое для остальных
расширений
• После рассортировки выводится сообщение типа «в папке с
текстовыми файлами перемещено 5 файлов, их суммарный
размер – 50 гигабайт»
• Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод сообщения
типа «Файл data.txt был переименован в some_data.txt»
• Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами.
'''

import os

# Вывести имя вашей ОС
os_name = os.name
print(os_name)

# Вывести путь до папки, в которой вы находитесь
current_directory = os.getcwd()

print(f"Текущий путь до папки: {current_directory}")


'''Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются все
файлы с расширением .txt, то же самое для остальных
расширений'''

import shutil
import random


def sort_files_by_extension(directory):
    summary = {}
    moved_files = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            extension_folder = os.path.join(directory, extension[1:])
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            shutil.move(filepath, os.path.join(extension_folder, filename))

            file_size = os.path.getsize(filepath)
            if extension not in summary:
                summary[extension] = {'count': 0, 'size': 0}
                moved_files[extension] = []
            summary[extension]['count'] += 1
            summary[extension]['size'] += file_size
            moved_files[extension].append(filename)

    for ext, data in summary.items():
        size_in_gb = data['size'] / (1024 ** 3)
        print(
            f"В папке с файлами типа {ext} перемещено {data['count']} файлов, их суммарный размер – {size_in_gb:.2f} гигабайт.")

        if moved_files[ext]:
            old_filename = random.choice(moved_files[ext])
            old_filepath = os.path.join(directory, ext[1:], old_filename)
            new_filename = f"some_{old_filename}"
            new_filepath = os.path.join(directory, ext[1:], new_filename)

            os.rename(old_filepath, new_filepath)
            print(f"Файл {old_filename} был переименован в {new_filename}.")


sort_files_by_extension(current_directory)

