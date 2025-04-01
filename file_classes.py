# HW 27

from abc import ABC, abstractmethod
import json
import csv
import os


class AbstractFile(ABC):
    """
    Абстрактный класс для работы с файлами.
    Определяет интерфейс для чтения, записи и добавления данных в файлы.
    """
    
    @abstractmethod
    def read(self):
        """
        Абстрактный метод для чтения данных из файла.
        
        Returns:
            Any: Данные, прочитанные из файла.
        """
        pass
    
    @abstractmethod
    def write(self, data):
        """
        Абстрактный метод для записи данных в файл.
        
        Args:
            data (Any): Данные для записи в файл.
        """
        pass
    
    @abstractmethod
    def append(self, data):
        """
        Абстрактный метод для добавления данных в файл.
        
        Args:
            data (Any): Данные для добавления в файл.
        """
        pass

class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    """
    
    def __init__(self, file_path: str):
        """
        Инициализация объекта JsonFile.
        
        Args:
            file_path (str): Путь к JSON-файлу.
        """
        self.file_path = file_path
    
    def read(self):
        """
        Чтение данных из JSON-файла.
        
        Returns:
            dict/list: Данные из JSON-файла.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    
    def write(self, data):
        """
        Запись данных в JSON-файл.
        
        Args:
            data (dict/list): Данные для записи в JSON-файл.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    
    def append(self, data):
        """
        Добавление данных в JSON-файл.
        
        Args:
            data (dict/list): Данные для добавления в JSON-файл.
        """
        existing_data = self.read()
        
        if isinstance(existing_data, list) and isinstance(data, list):
            existing_data.extend(data)
        elif isinstance(existing_data, dict) and isinstance(data, dict):
            existing_data.update(data)
        elif isinstance(existing_data, list):
            existing_data.append(data)
        else:
            # Если файл пуст или содержит некорректные данные
            existing_data = data
        
        self.write(existing_data)