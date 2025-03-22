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