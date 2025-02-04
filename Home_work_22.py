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
        return file.readlines()

def read_csv (file_path: str, encoding: str = "utf-8") -> None:
    pass

def read_json (file_path: str, encoding: str = "utf-8") -> None:
    pass

def read_yaml (file_path: str, encoding: str = "utf-8") -> None:
    pass


def write_txt (*data: str, file_path: str, encoding: str = "utf-8") -> None:
    pass

def write_csv (*data: dict, delimetr: str = ";", file_path: str, encoding: str = "utf-8") -> None:
    pass

def write_json (*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    pass

def append_txt (*data: str, file_path: str, encoding: str = "utf-8") -> None:
    pass

def append_csv (*data: dict, delimetr: str = ";", file_path: str, encoding: str = "utf-8") -> None:
    pass

def append_json (*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    pass


