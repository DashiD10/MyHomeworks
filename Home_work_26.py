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