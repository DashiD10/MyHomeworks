class TxtHandler:
        """
    Класс для работы с текстовыми файлами
    Methods:
        1. read() ->List[str]: возвращает список строк из файла
        2. write(data: List[str]) -> None: записывает список строк в файл
        3. append(data: List[str]) -> None: добавляет список строк в конец Exceptions:
    FileNotFoundError: если файл не найден
    PermissionError: если нет прав на запись
        """