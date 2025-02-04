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

def read_csv (file_path: str, encoding: str = "utf-8") -> None:
    pass

def read_json (file_path: str, encoding: str = "utf-8") -> None:
    pass

def read_yaml (file_path: str, encoding: str = "utf-8") -> None:
    pass



def write_txt (*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """
    Функция записывает данные в файл

    : param data: Данные для записи
    : param file_path: путь к файлу
    :param encoding: кодировка файла
    """
    with open(file_path, "w", encoding=encoding) as file:
        ready_data = [item + '\n' for item in data]
        file.writelines(ready_data)

def write_csv (*data: dict, delimetr: str = ";", file_path: str, encoding: str = "utf-8") -> None:
    pass

def write_json (*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    pass

def append_txt (*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """
    Функция для добавления данных в текстовый файл.

    :param data: Данные для добавления.
    :param file_path: Путь к файлу
    :param encoding: Кодировка файла
    """
    with open(file_path, "a", encoding=encoding) as file:
        ready_data = [item + '\n' for item in data]
        file.writelines(ready_data)

def append_csv (*data: dict, delimetr: str = ";", file_path: str, encoding: str = "utf-8") -> None:
    pass

def append_json (*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    pass


