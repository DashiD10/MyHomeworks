from file_classes import JsonFile, TxtFile, CsvFile
import os


def test_json_file():
    """Тестирование класса JsonFile."""
    print("\n=== Тестирование JSON файла ===")
    
    # Создаем экземпляр класса JsonFile
    json_file = JsonFile("test_data.json")
    
    # Записываем данные в файл
    test_data = {"name": "John", "age": 30, "city": "New York"}
    json_file.write(test_data)
    print(f"Записаны данные: {test_data}")
    
    # Читаем данные из файла
    read_data = json_file.read()
    print(f"Прочитаны данные: {read_data}")
    
    # Добавляем данные в файл
    append_data = {"email": "john@example.com", "phone": "123-456-7890"}
    json_file.append(append_data)
    print(f"Добавлены данные: {append_data}")
    
    # Проверяем результат
    final_data = json_file.read()
    print(f"Итоговые данные: {final_data}")


def test_txt_file():
    """Тестирование класса TxtFile."""
    print("\n=== Тестирование TXT файла ===")
    
    # Создаем экземпляр класса TxtFile
    txt_file = TxtFile("test_data.txt")
    
    # Записываем данные в файл
    test_data = "Это тестовая строка для записи в файл."
    txt_file.write(test_data)
    print(f"Записаны данные: {test_data}")
    
    # Читаем данные из файла
    read_data = txt_file.read()
    print(f"Прочитаны данные: {read_data}")
    
    # Добавляем данные в файл
    append_data = "\nЭто дополнительная строка для добавления в файл."
    txt_file.append(append_data)
    print(f"Добавлены данные: {append_data}")
    
    # Проверяем результат
    final_data = txt_file.read()
    print(f"Итоговые данные: {final_data}")


def test_csv_file():
    """Тестирование класса CsvFile."""
    print("\n=== Тестирование CSV файла ===")
    
    # Создаем экземпляр класса CsvFile
    csv_file = CsvFile("test_data.csv")
    
    # Записываем данные в файл
    test_data = [
        ["Имя", "Возраст", "Город"],
        ["Иван", "25", "Москва"],
        ["Мария", "30", "Санкт-Петербург"]
    ]
    csv_file.write(test_data)
    print(f"Записаны данные: {test_data}")
    
    # Читаем данные из файла
    read_data = csv_file.read()
    print(f"Прочитаны данные: {read_data}")
    
    # Добавляем данные в файл
    append_data = [["Алексей", "35", "Казань"]]
    csv_file.append(append_data)
    print(f"Добавлены данные: {append_data}")
    
    # Проверяем результат
    final_data = csv_file.read()
    print(f"Итоговые данные: {final_data}")


def cleanup():
    """Удаление тестовых файлов."""
    test_files = ["test_data.json", "test_data.txt", "test_data.csv"]
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Файл {file} удален.")


if __name__ == "__main__":
    # Тестируем все классы
    test_json_file()
    test_txt_file()
    test_csv_file()
    
    # Спрашиваем пользователя, хочет ли он удалить тестовые файлы
    answer = input("\nУдалить тестовые файлы? (y/n): ")
    if answer.lower() == 'y':
        cleanup()