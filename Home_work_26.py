"""
Модуль для сжатия изображений в формат HEIF с использованием ООП.
"""

import os

from typing import Tuple
from PIL import Image
from pillow_heif import register_heif_opener


class ImageCompressor:
    """
    Класс для сжатия изображений и их сохранения в формате HEIF.
    
    Attributes:
        supported_formats (Tuple[str, ...]): Поддерживаемые форматы изображений.
    """
    
    supported_formats: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')

    def __init__(self, quality: int = 50):
        """
        Инициализирует объект ImageCompressor.
        
        Args:
            quality (int): Качество сжатия изображения (1-100).
                По умолчанию 50.
        """
        self.__quality = quality
        register_heif_opener()
    
    @property
    def quality(self) -> int:
        """
        Геттер для получения текущего значения качества сжатия.
        
        Returns:
            int: Текущее значение качества сжатия.
        """
        return self.__quality
    
    @quality.setter
    def quality(self, quality: int) -> None:
        """
        Сеттер для установки значения качества сжатия.
        
        Args:
            quality (int): Новое значение качества сжатия (1-100).
        """
        if not isinstance(quality, int):
            raise TypeError("Качество должно быть целым числом")
        if quality < 1 or quality > 100:
            raise ValueError("Качество должно быть в диапазоне от 1 до 100")
        self.__quality = quality

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.
        
        Args:
            input_path (str): Путь к исходному изображению.
            output_path (str): Путь для сохранения сжатого изображения.
        """
        try:
            with Image.open(input_path) as img:
                img.save(output_path, "HEIF", quality=self.__quality)
            print(f"Сжато: {input_path} -> {output_path}")

        except (IOError, OSError, Image.UnidentifiedImageError) as e:
            print(f"Ошибка при сжатии {input_path}: {e}")
    
    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.
        
        Args:
            directory (str): Путь к директории для обработки.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                # Проверяем расширение файла
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)

def main(input_path: str) -> None:
    """
    Основная функция программы. Обрабатывает входной путь и запускает сжатие изображений.
    
    Args:
        input_path (str): Путь к файлу или директории для обработки.
    """
    # Создаем экземпляр класса ImageCompressor с качеством сжатия 50
    compressor = ImageCompressor(quality=50)
    
    input_path = input_path.strip('"')  # Удаляем кавычки, если они есть
    
    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            # Если указан путь к файлу, обрабатываем только этот файл
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + '.heic'
            compressor.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            # Если указан путь к директории, обрабатываем все файлы в ней
            print(f"Обрабатываем директорию: {input_path}")
            compressor.process_directory(input_path)
    else:
        print("Указанный путь не существует")


if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    main(user_input)