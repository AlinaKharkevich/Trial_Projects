import os
import re
import sys
from typing import List, Dict, Callable

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = os.path.join(CURRENT_DIR, "data.txt")
PAGE_SIZE = 10
  
def welcome() -> None:
    """Выводит приветственное сообщение и список доступных команд."""
    print("Добро пожаловать в телефонную справочник!")
    print("Выберите команду:")
    print("0 - Выход из справочника.")
    print("1 - Выводит записи из справочника постранично.")
    print("2 - Добавляет новую запись в справочник.")
    print("3 - Редактирует выбранную запись в справочнике.")
    print("4 - Ищет запись в справочнике.")

def exit_program() -> None:
    """Выход из справочника."""
    """
    Печатает прощальное сообщение и завершает программу.

    """
    print("Вы решили покинуть справочник. До свидания!")
    sys.exit(0)

def show_records() -> None:
    """Выводит записи из справочника постранично."""
    """
    Если файл справочника не существует, печатает сообщение "Файл не найден.".
    Если записей в справочнике нет, печатает сообщение "Справочник пуст.".
    Иначе, выводит записи постранично и позволяет пользователю просматривать следующие страницы нажав Enter или остановить просмотр введя '9'.

    """
    if not os.path.exists(FILE_PATH): # Проверка наличия файла
        print("Файл не найден.")
        return
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        lines: List[str] = file.readlines()
        if not lines or all(not line.strip() for line in lines): # Проверка наличия записей в справочнике
            print("Справочник пуст.")
            return
        
        page_num: int = 1
        start_index: int = (page_num - 1) * PAGE_SIZE
        end_index: int = min(start_index + PAGE_SIZE, len(lines))

        while start_index < len(lines):
            print("\n".join(lines[start_index:end_index]))
            print("Номер страницы:", page_num)  # Вывод номера текущей страницы
            if end_index >= len(lines):
                print("Конец справочника.")
                break

            command: str = input("\nНажмите Enter для вывода следующей страницы или введите '9' для остановки просмотра страниц: \n")
            if command == "9": # Пользователь не хочет смотреть следующие страницы (работает только при их наличиии)
                break
            elif command != "":
                print("Неверная команда. Пожалуйста, попробуйте снова.")
                break
            page_num += 1
            start_index = (page_num - 1) * PAGE_SIZE
            end_index = min(start_index + PAGE_SIZE, len(lines))

def validate_input(prompt: str, regex: str) -> str:
    """Проверяет введенное значение на соответствие регулярному выражению."""
    """
    Args:
        prompt: Ввод от пользователя.
        regex: Регулярное выражение для проверки значения.
    Returns:
        Введенное пользователем значение, если оно соответствует регулярному выражению.

    """
    while True:
        user_input: str = input(prompt)
        if re.match(regex, user_input):
            return user_input
        else:
            print("Неправильный формат. Пожалуйста, попробуйте снова.")


def add_record() -> None:
    """Добавляет новую запись в справочник."""
    """
    Если файл справочника не существует, печатает сообщение "Файл не найден.".
    Проверяет введенные пользователем данные на соответствие заданным регулярным выражениям.
    Если запись уже существует, печатает сообщение "Такая запись уже существует.".
    Иначе, добавляет запись в файл и печатает сообщение "Запись добавлена успешно.".

    """
    if not os.path.exists(FILE_PATH): # Проверка наличия файла
        print("Файл не найден.")
        return
    with open(FILE_PATH, "r", encoding='utf-8') as file:
        lines = file.readlines()
        last_name = validate_input("Введите фамилию: ", r"^[А-ЯЁ][а-яё]+$") # C большой буквы, русскими буквами
        first_name = validate_input("Введите имя: ", r"^[А-ЯЁ][а-яё]+$")
        middle_name = validate_input("Введите отчество: ", r"^[А-ЯЁ][а-яё]+$")
        organization = validate_input("Введите название организации: ", r".+")
        
        work_phone = validate_input("Введите рабочий телефон в формате +7хххххххххх: ", r"\+7\d{10}$") # Номер начинается с "+7" и содержит 10 цифр после этого
        personal_phone = validate_input("Введите личный телефон в формате +7хххххххххх: ", r"\+7\d{10}$")

        entry = f"{last_name} {first_name} {middle_name} {organization} {work_phone} {personal_phone}"
        duplicate = any(entry == line.strip() for line in lines)  # Проверяем, есть ли такая же запись в файле
        if duplicate:
            print("Такая запись уже существует.")
            return
    with open(FILE_PATH, "a", encoding='utf-8') as file:
        file.write("\n" + f"{entry}")
    print("Запись добавлена успешно.")

def search_record() -> str: 
    """Ищет запись в справочнике."""
    """
    Если файл справочника не существует, печатает сообщение "Файл не найден.".
    Returns:
        str: Строка с найденной записью или None, если "Такой записи не найдено.".
    """
    if not os.path.exists(FILE_PATH): # Проверка наличия файла
        print("Файл не найден.")
        return
    found: bool = False
    last_name = validate_input("Введите фамилию: ", r"^[А-ЯЁ][а-яё]+$") # C большой буквы, русскими буквами
    personal_phone = validate_input("Введите личный телефон в формате +7хххххххххх: ", r"\+7\d{10}$") # Номер начинается с "+7" и содержит 10 цифр после этого

    with open(FILE_PATH, "r", encoding="utf-8") as file: 
        for line in file: 
            record = line.strip().split(",") 
            if record[0] == last_name and record[5] == personal_phone: 
                print(line) 
                found = True
                return line.strip()
    if not found:    
        print("Такой записи не найдено.")
        return None
    
def edit_record() -> None:
    """Редактирует выбранную запись в справочнике."""
    """
    Если файл справочника не существует, печатает сообщение "Файл не найден.".
    Запрашивает у пользователя поле для исправления: рабочий телефон(ввод'7') или личный телефон(ввод '8')
    Если данные неверны, то печатает "Некорректно выбрано поле для исправления."
    Запрашивает у пользователя новые данные на замену, открывает файл для чтения и записи, производит исправление записи.
    Сохраняет изменения в файле и печатает сообщение "Запись успешно исправлена.".

    """
    if not os.path.exists(FILE_PATH): # Проверка наличия файла
        print("Файл не найден.")
        return
    
    record: str = search_record()
    if record is not None:
        field_to_edit: str = input("Выберите поле для исправления: рабочий телефон(нажми '7') или личный телефон(нажми '8'): ")
        new_data: str = validate_input("Введите новые данные в формате +7хххххххххх: ", r"\+7\d{10}$")
        
        with open(FILE_PATH, "r+", encoding="utf-8") as file:
            lines: List[str] = file.readlines()
            for i, line in enumerate(lines):
                if line.strip() == record:
                    if field_to_edit == "7": # Рабочий телефон
                        fields: List[str] = line.strip().split(",")
                        fields[4] = new_data
                        lines[i] = ",".join(fields) + "\n"
                    elif field_to_edit == "8": # Личный телефон
                        fields: List[str] = line.strip().split(",")
                        fields[5] = new_data
                        lines[i] = ",".join(fields) + "\n"
                    else:
                        print("Некорректно выбрано поле для исправления.")
                        return      
            file.seek(0)
            file.writelines(lines)
        print("Запись успешно исправлена.")

def main() -> None:
    """Основная функция программы."""
    """
    Инициализирует словарь с командами и соответствующими функциями,
    Выводит приветственное сообщение пользователю,
    В цикле запрашивает у пользователя команду и вызывает соответствующую функцию, если команда верна. 
    В случае неверной команды выводит сообщение "Неверная команда. Пожалуйста, попробуйте снова."

    """
    commands: Dict[str, Callable[[], None]] = { # Словарь
        "0": exit_program,
        "1": show_records,
        "2": add_record,
        "3": edit_record,
        "4": search_record
    }
    welcome()
    while True:
        command: str = input("\nВведите номер команды: ")
        if command in commands:
            commands[command]()
        else:
            print("Неверная команда. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()