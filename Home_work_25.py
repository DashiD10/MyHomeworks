from typing import Tuple, List


class TxtHandler:
    #     """
    # Класс для работы с текстовыми файлами
    # Methods:
    #     1. read() ->List[str]: возвращает список строк из файла
    #     2. write(*data: Tuple[str, ...]) -> None: записывает список строк в файл
    #     3. append(*data: Tuple[str, ...]) -> None: добавляет список строк в конец Exceptions:
    # FileNotFoundError: если файл не найден
    # PermissionError: если нет прав на запись
    #     """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> List[str]:
        """
        Читает данные из файла и возвращает список строкю
        :return: Список строк из файла.
        :raise FileNotFoundError: Если файл не найден.
        :raise PermissionError: Если нет прав на чтение файла.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                row_data = file.readlines()
                return [row.strip() for row in row_data]
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден.")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {self.file_path}.")

    def write(self, *data: str) -> None:
        """
        Записывает список строк в файл.
        :param data: Список строк для записи в файл.
        :raise PermissionError: Если нет прав на запись в файл.
        """
        prepared_data = [line + "\n" for line in data]
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.writelines(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}.")

    def append(self, *data: str) -> None:
        """
        Добавляет список строк в конец файла.
        :param data: Список строк для добавления в файл.
        :raise PermissionError: Если нет прав на запись в файл.
        """
        prepared_data = [line + "\n" for line in data]
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.writelines(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}.")


if __name__ == "__main__":
    txt_handler = TxtHandler("Home_work_25.txt")
    txt_handler.write("Hello", " World")
    txt_handler.append(" Запишем еще строку", " и еще одну")
    print(txt_handler.read())


import json
import csv
from typing import List, Dict, Any


class TxtFileHandler:
    def read_file(self, filepath: str) -> str:
        """
        Читает данные из TXT файла.

        Args:
            filepath: Путь к файлу

        Returns:
            Содержимое файла в виде строки
        """
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def write_file(self, filepath: str, *data: str) -> None:
        """
        Записывает данные в TXT файл.

        Args:
            filepath: Путь к файлу
            data: Строки для записи
        """
        with open(filepath, "w", encoding="utf-8") as file:
            file.writelines(data)

    def append_file(self, filepath: str, *data: str) -> None:
        """
        Добавляет данные в конец TXT файла.

        Args:
            filepath: Путь к файлу
            data: Строки для добавления
        """
        with open(filepath, "a", encoding="utf-8") as file:
            file.writelines(data)


class CSVFileHandler:
    def read_file(self, filepath: str) -> List[Dict]:
        """
        Читает данные из CSV файла.

        Args:
            filepath: Путь к файлу

        Returns:
            Список словарей с данными из CSV
        """
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            return []

    def write_file(self, filepath: str, data: List[Dict]) -> None:
        """
        Записывает список словарей в CSV файл.

        Args:
            filepath: Путь к файлу
            data: Список словарей для записи
        """
        if not data:
            return

        with open(filepath, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def append_file(self, filepath: str, data: List[Dict]) -> None:
        """
        Добавляет список словарей в конец CSV файла.

        Args:
            filepath: Путь к файлу
            data: Список словарей для добавления
        """
        try:
            with open(filepath, "a", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writerows(data)
        except FileNotFoundError:
            self.write_file(filepath, data)


class JSONFileHandler:
    def read_file(self, filepath: str) -> List[Dict]:
        """
        Читает данные из JSON файла.

        Args:
            filepath: Путь к файлу

        Returns:
            Список словарей из JSON файла
        """
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_file(self, filepath: str, data: List[Dict]) -> None:
        """
        Записывает список словарей в JSON файл.

        Args:
            filepath: Путь к файлу
            data: Список словарей для записи
        """
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def append_file(self, filepath: str, data: List[Dict]) -> None:
        """
        Добавляет данные в JSON файл.

        Args:
            filepath: Путь к файлу
            data: Список словарей для добавления
        """
        try:
            existing_data = self.read_file(filepath)
            if isinstance(existing_data, list):
                existing_data.extend(data)
            else:
                existing_data = data
            self.write_file(filepath, existing_data)
        except FileNotFoundError:
            self.write_file(filepath, data)


# Пример использования
if __name__ == "__main__":
    # Работа с TXT файлами
    txt_handler = TxtFileHandler()
    txt_handler.write_file("example.txt", "Начало файла.\n")
    txt_handler.append_file("example.txt", "Добавляем строку.\n")
    content_txt = txt_handler.read_file("example.txt")
    print("Содержимое TXT:\n", content_txt)

    # Работа с CSV файлами
    csv_handler = CSVFileHandler()
    data_csv = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
    csv_handler.write_file("example.csv", data_csv)
    csv_handler.append_file("example.csv", [{"name": "Charlie", "age": "35"}])
    content_csv = csv_handler.read_file("example.csv")
    print("Содержимое CSV:\n", content_csv)

    # Работа с JSON файлами
    json_handler = JSONFileHandler()
    data_json = [
        {"product": "Laptop", "price": 1500},
        {"product": "Phone", "price": 800},
    ]
    json_handler.write_file("example.json", data_json)
    json_handler.append_file("example.json", [{"product": "Tablet", "price": 600}])
    content_json = json_handler.read_file("example.json")
    print("Содержимое JSON:\n", content_json)
