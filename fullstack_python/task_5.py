import json
import os
import csv


def load_employees(json_file_path):
    """ Загружает данные о сотрудниках из JSON-файла. """
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    else:
        print("Файл не найден.")
        return []


def add_employee_to_json(json_file_path):
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            employees = json.load(json_file)
    else:
        employees = []

    # Сбор данных о новом сотруднике
    name = input("Введите имя сотрудника: ")
    birthday = input("Введите дату рождения сотрудника (ДД.ММ.ГГГГ): ")
    height = float(input("Введите рост сотрудника (см): "))
    weight = float(input("Введите вес сотрудника (кг): "))
    car = input("Есть ли у сотрудника автомобиль? (да/нет): ").strip().lower() == 'да'
    languages = input("Введите языки программирования, через запятую: ").split(',')

    new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": [lang.strip() for lang in languages]
    }

    employees.append(new_employee)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(employees, json_file, ensure_ascii=False, indent=4)

    print(f"Сотрудник {name} успешно добавлен в '{json_file_path}'.")


def add_employee_to_csv(csv_file_path):
    file_exists = os.path.exists(csv_file_path)

    # Сбор данных о новом сотруднике
    name = input("Введите имя сотрудника: ")
    birthday = input("Введите дату рождения сотрудника (ДД.ММ.ГГГГ): ")
    height = float(input("Введите рост сотрудника (см): "))
    weight = float(input("Введите вес сотрудника (кг): "))
    car = input("Есть ли у сотрудника автомобиль? (да/нет): ").strip().lower() == 'да'
    languages = input("Введите языки программирования, через запятую: ").split(',')

    languages = [lang.strip() for lang in languages]
    languages_str = ', '.join(languages)

    with open(csv_file_path, 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if not file_exists:
            writer.writerow(["name", "birthday", "height", "weight", "car", "languages"])

        writer.writerow([name, birthday, height, weight, car, languages_str])

    print(f"Сотрудник {name} успешно добавлен в '{csv_file_path}'.")


def find_employee_by_name(employees, name):
    """ Находит информацию о сотруднике по имени. """
    for employee in employees:
        if employee['name'].lower() == name.lower():
            return employee
    return None


def filter_employees_by_language(employees, language):
    """ Выводит всех сотрудников, владеющих указанным языком программирования. """
    return [employee for employee in employees if language in employee['languages']]


def filter_employees_by_year(employees, year):
    """ Вычисляет средний рост сотрудников, родившихся до указанного года. """
    total_height = 0
    count = 0
    for employee in employees:
        birth_year = int(employee['birthday'].split('.')[-1])
        if birth_year < year:
            total_height += employee['height']
            count += 1

    if count == 0:
        return None
    return total_height / count


def save_to_csv(employees, csv_file_path):
    """ Сохраняет данные о сотрудниках в CSV-файл. """
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = employees[0].keys()
        writer = csv.DictWriter('employees.csv', fieldnames=fieldnames)

        writer.writeheader()
        for employee in employees:
            writer.writerow(employee)


def json_to_csv(input_json_path, output_csv_path):
    """ Преобразует JSON-файл в CSV-файл. """
    employees = load_employees(input_json_path)
    if employees:
        save_to_csv(employees, output_csv_path)
        print(f"Данные успешно сохранены в {output_csv_path}.")
    else:
        print("Не удалось преобразовать данные, так как они отсутствуют.")


def main_menu(employees):
    while True:
        print("\n-- Меню --")
        print("1. Найти сотрудника по имени")
        print("2. Вывести сотрудников по языку программирования")
        print("3. Вычислить средний рост сотрудников по году рождения")
        print("4. Экспорт сотрудников в CSV")
        print("5. Добавить нового сотрудника в JSON")
        print("6. Добавить нового сотрудника в CSV")
        print("7. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            name = input("Введите имя сотрудника для поиска: ")
            employee = find_employee_by_name(employees, name)
            if employee:
                print("Информация о сотруднике:", employee)
            else:
                print("Сотрудник с таким именем не найден.")

        elif choice == '2':
            language = input("Введите язык программирования для фильтрации: ")
            filtered_employees = filter_employees_by_language(employees, language)
            if filtered_employees:
                print("Сотрудники, владеющие языком", language, ":")
                for emp in filtered_employees:
                    print(emp)
            else:
                print("Нет сотрудников, владеющих языком", language)

        elif choice == '3':
            year = int(input("Введите год рождения для фильтрации: "))
            average_height = filter_employees_by_year(employees, year)
            if average_height is not None:
                print(f"Средний рост сотрудников, родившихся до {year} года: {average_height:.2f} см.")
            else:
                print(f"Нет сотрудников, родившихся до {year} года.")

        elif choice == '4':
            input_json_path = 'employees.json'
            output_csv_path = 'employees.csv'
            json_to_csv(input_json_path, output_csv_path)

        elif choice == '5':
            add_employee_to_json('employees.json')

        elif choice == '6':
            add_employee_to_csv('employees.csv')


        elif choice == '7':
            print("Выход из программы.")

            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт из меню.")

# Путь к JSON-файлу
json_file_path = './data.json'
output_csv_path = './'
# Загружаем данные о сотрудниках
employees = load_employees(json_file_path)

if employees:
    main_menu(employees)
else:
    print("Не удалось загрузить данные о сотрудниках. Проверьте файл JSON.")


load_employees(json_file_path)