# task 1
'''
На вход принимается значение, равное одному из элементов списка.
Реализовать функцию, выполняющую рекурсивный алгоритм
бинарного поиска, на выходе программа должна вывести позицию
искомого элемента в исходном списке.
'''


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    # Элемент не найден
    return -1


# Функция для запуска бинарного поиска
def search(arr, x):
    return binary_search(arr, 0, len(arr) - 1, x)


# Пример использования
    # sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # search_value = 5
    # result = search(sorted_list, search_value)

    # if result != -1:
    #     print(f"Элемент {search_value} найден на позиции {result}.")
    # else:
    #     print(f"Элемент {search_value} не найден в списке.")

# task 2
'''
    Программа получает на вход число в десятичной системе
счисления. Реализовать функцию, которая переводит входное
число в двоичную систему счисления. Допускается реализация
функции как в рекурсивном варианте, так и с итеративным
подходом.
'''
def to_binary(num):


    binary = ""

    while int(num) > 0:
        if int(num) % 2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num = int(num) // 2

    return binary

def decimal_to_binary_rec(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary_rec(n // 2) + str(n % 2)


# Пример использования
decimal_number = 42
binary_number = to_binary(decimal_number)
print(f"Десятичное число: {decimal_number}")
print(f"Двоичное число: {binary_number}")

# task 3
'''
    Программа получает на вход число. Реализовать функцию,
которая определяет, является ли это число простым (делится
только на единицу и на само себя).
'''
def is_simple(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True

#task 4
'''
    Программа получает на вход два числа и находит их НОД
(наибольший общий делитель). Пример: на вход подаются числа 12 и 18, их НОД равен 6.
'''
def find_deviser(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = find_deviser(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}")

#task 5
'''
    Программа получает на вход строку – сообщение и
указание, что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное сообщение
шифром Цезаря, вторая – расшифровывает. В зависимости от
выбора пользователя (шифровать или дешифровать) вызывается
соответствующая функция, результат выводится в консоль.
'''
def caesar_cipher(message, shift, encrypt=True):
    result = ''
    for char in message:
        if char.isalpha():
            alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' if char.islower() else 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            result += alphabet[(alphabet.index(char) + shift) % len(alphabet) if encrypt else (alphabet.index(char) - shift) % len(alphabet)]
        else:
            result += char
    return result

message = input("Введите сообщение: ")
mode = input("Выберите режим (шифровать/дешифровать): ")
shift = int(input("Введите сдвиг: "))

if mode.lower() == 'шифровать':
    print("Зашифрованное сообщение:", caesar_cipher(message, shift, encrypt=True))
elif mode.lower() == 'дешифровать':
    print("Расшифрованное сообщение:", caesar_cipher(message, shift, encrypt=False))
else:
    print("Неверный режим.")

# 7
import random
'''
    Реализовать функцию, которая создаёт матрицу размером
M строк на N столбцов и заполняет её рандомными числами.
'''
def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix
create_matrix(2, 3)

# task 8
'''
     Реализовать функцию, которая находит минимальный и
максимальный элементы в матрице (матрица M x N). Вывести в
консоль индексы найденных элементов.
'''
def find_min_max(matrix):
    min_val = float('inf')
    max_val = float('-inf')
    min_idx = (0, 0)
    max_idx = (0, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_idx = (i, j)
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_idx = (i, j)

    print(f"Минимальный элемент: {min_val} (индекс: {min_idx})")
    print(f"Максимальный элемент: {max_val} (индекс: {max_idx})")

# task 9
'''
     Реализовать функцию, которая находит сумму элементов
матрицы (матрица M x N). Определить, какую долю в общей сумме (процент) составляет сумма элементов каждого столбца.
'''
def calculate_matrix_sum_and_column_percentages(matrix):
    # Вычисляем сумму всех элементов матрицы
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)

    column_sums = [0] * len(matrix[0])
    for row in matrix:
        for i, element in enumerate(row):
            column_sums[i] += element

    # Вычисляем процент суммы каждого столбца от общей суммы
    column_percentages = [(column_sum / total_sum) * 100 for column_sum in column_sums]
    print(f"Общая сумма элементов матрицы: {total_sum}")
    for i, percentage in enumerate(column_percentages):
        print(f"Сумма элементов {i + 1}-го столбца: {column_sums[i]} ({percentage:.2f}% от общей суммы)")

    return total_sum, column_sums, column_percentages

# task 12
'''
    Программа получает на вход число H. Реализовать
функцию, которая определяет, какие столбцы имеют хотя бы одно
такое же число, а какие не имеют (матрица M x N).
'''
def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix


def find_matching_columns(matrix, num):
    matching_columns = []
    non_matching_columns = []

    for col_idx in range(len(matrix[0])):
        has_match = False
        for row_idx in range(len(matrix)):
            if matrix[row_idx][col_idx] == num:   # тут ведь так должно быть [row_idx][col_idx], а не наоборот - [col_idx][row_idx] ?
                has_match = True
                break
        if has_match:
            matching_columns.append(col_idx)
        else:
            non_matching_columns.append(col_idx)

    return matching_columns, non_matching_columns

# task 13
'''
    Реализовать функцию, которая находит сумму элементов
на главной диагонали и сумму элементов на побочной диагонали
(матрица M x N).
'''
def create_matrix_13(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix


def calculate_diagonal_sums(matrix):
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(len(matrix)):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][len(matrix) - 1 - i]

    return main_diagonal_sum, secondary_diagonal_sum

# task 14
'''
    Дана матрица M x N. Исходная матрица состоит из нулей и
единиц. Реализовать функцию, которая добавит к матрице ещё
один столбец, элементы которого делает количество единиц в
соответствующей строке чётным.
'''
def create_matrix_14(rows, cols):
    matrix_14 = []
    for _ in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        matrix_14.append(row)
    return matrix_14

def make_even_ones(matrix):
    new_matrix_14 = []
    for row in matrix:
        ones_count = sum(row)
        if ones_count % 2 == 0:
            new_row = row + [0]
        else:
            new_row = row + [1]
        new_matrix_14.append(new_row)
    return new_matrix_14