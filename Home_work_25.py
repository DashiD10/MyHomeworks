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
