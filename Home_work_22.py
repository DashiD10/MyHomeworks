import csv
import json
import yaml


def read_txt (file_path: str, encoding: str = "utf-8") -> list[str]:
    """
    Функция читает файл 

    :param file_path: путь к файлу
    :param encoding: кодировка файла
    :return: список строк из файла
    """
    with open(file_path, "r", encoding=encoding) as file:
        data = [item.rstrip("\n") for item in file.readlines()]
        return data


def read_csv (file_path: str, encoding: str = "utf-8") -> list[dict]:
    """
    Функция для чтения csv файла.

    :param file_path: путь к файлу
    :param delimiter: разделитель
    :param encoding: кодировка файла
    :return: список словарей
    """
    with open(file_path, "r", encoding=encoding) as file:
        data = csv.DictReader(file, delimiter=delimiter)
        return list(data)

def read_json (file_path: str, encoding: str = "utf-8") -> list[dict]:
    """
    Функция для чтения json файла.

    :param file_path: путь к файлу
    :param encoding: кодировка файла
    :return: список словарей
    """
    with open(file_path, "r", encoding=encoding) as file:
        data = json.load(file)
        return data

def read_yaml (file_path: str, encoding: str = "utf-8") -> None:
    pass


def write_txt (file_path: str, *data: str, encoding: str = "utf-8") -> None:
    """
    Функция записывает данные в файл

    : param data: Данные для записи
    : param file_path: путь к файлу
    :param encoding: кодировка файла
    """
    with open(file_path, "w", encoding=encoding) as file:
        ready_data = [item + '\n' for item in data]
        file.writelines(ready_data)

def write_csv (file_path: str, *data: dict, delimetr: str = ";", encoding: str = "utf-8-sig"):
    """
    Функция для записи данных в csv файл.

    :param file_path: Путь к файлу
    :param data: Данные для записи
    :param delimetr: Разделитель
    :param encoding: Кодировка файла
    """
    with open(file_path, "w", encoding=encoding) as file:
        writer = csv.DictWriter(file, delimiter=delimetr, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def write_json (file_path: str, *data: dict, encoding: str = "utf-8") -> None:
    """
    Функция для записи данных в json файл.

    :param file_path: Путь к файлу
    :param data: Данные для записи
    :param encoding: Кодировка файла
    """
    with open(file_path, "w", encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def write_yaml (file_path: str, *data: dict, encoding: str = "utf-8") -> None:
    pass

def append_txt (file_path: str, *data: str, encoding: str = "utf-8") -> None:
    """
    Функция для добавления данных в текстовый файл.

    :param data: Данные для добавления.
    :param file_path: Путь к файлу
    :param encoding: Кодировка файла
    """
    with open(file_path, "a", encoding=encoding) as file:
        ready_data = [item + '\n' for item in data]
        file.writelines(ready_data)

def append_csv (file_path: str, *data: dict, delimetr: str = ";", encoding: str = "utf-8") -> None:
    """
    Функция для добавления данных в csv файл.

    :param file_path: Путь к файлу
    :param data: Данные для добавления
    :param delimetr: Разделитель
    :param encoding: Кодировка файла
    """
    with open(file_path, "a", encoding=encoding) as file:
        writer = csv.DictWriter(file, delimiter=delimetr, fieldnames=data[0].keys())
        writer.writerows(data)

def append_json (file_path: str, *data: dict, encoding: str = "utf-8") -> None:
    """
    Функция для добавления данных в json файл.
    В этом случае JSON перезаписывается, 
    используем уже написанные функции

    :param file_path: Путь к файлу
    :param data: Данные для добавления
    :param encoding: Кодировка файла
    """
    data_json = read_json(file_path)
    data_json.extend(data)
    write_json(file_path, data_json)


