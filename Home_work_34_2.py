import sqlite3
from typing import List, Tuple, Optional

# Константы
DATABASE_PATH = "barbershop.db"
SQL_SCRIPT_PATH = "Home_work_34_1.sql"


def read_sql_file(filepath: str) -> str:
    """Читает текст SQL-скрипта из файла и возвращает его содержимое."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def execute_script(conn: sqlite3.Connection, script: str) -> None:
    """Принимает соединение и текст скрипта, создаёт курсор, выполняет скрипт через метод executescript, сохраняет изменения."""
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()


def find_appointment_by_phone(conn: sqlite3.Connection, phone: str) -> List[Tuple]:
    """Принимает соединение и номер телефона, выполняет параметризованный SELECT-запрос на точное совпадение номера телефона."""
    cursor = conn.cursor()
    query = """
    SELECT 
        a.id,
        a.name,
        a.phone,
        a.date,
        m.first_name || ' ' || m.last_name AS master_name,
        GROUP_CONCAT(s.title, ', ') AS services,
        a.status,
        a.comment
    FROM appointments a
    LEFT JOIN masters m ON a.master_id = m.id
    LEFT JOIN appointments_services aps ON a.id = aps.appointment_id
    LEFT JOIN services s ON aps.service_id = s.id
    WHERE a.phone = ?
    GROUP BY a.id
    ORDER BY a.date DESC
    """
    cursor.execute(query, (phone,))
    return cursor.fetchall()


def find_appointment_by_comment(conn: sqlite3.Connection, comment_part: str) -> List[Tuple]:
    """Принимает соединение и часть комментария, ищет записи, где комментарий содержит переданную строку."""
    cursor = conn.cursor()
    query = """
    SELECT 
        a.id,
        a.name,
        a.phone,
        a.date,
        m.first_name || ' ' || m.last_name AS master_name,
        GROUP_CONCAT(s.title, ', ') AS services,
        a.status,
        a.comment
    FROM appointments a
    LEFT JOIN masters m ON a.master_id = m.id
    LEFT JOIN appointments_services aps ON a.id = aps.appointment_id
    LEFT JOIN services s ON aps.service_id = s.id
    WHERE a.comment LIKE ?
    GROUP BY a.id
    ORDER BY a.date DESC
    """
    cursor.execute(query, (f'%{comment_part}%',))
    return cursor.fetchall()


def create_appointment(conn: sqlite3.Connection, client_name: str, client_phone: str, 
                      master_name: str, services_list: List[str], comment: str = None) -> int:
    """Создаёт новую запись в таблице клиентов."""
    cursor = conn.cursor()
    
    # Поиск мастера по имени (предполагаем формат "Имя Фамилия")
    name_parts = master_name.split()
    if len(name_parts) >= 2:
        first_name, last_name = name_parts[0], name_parts[1]
        cursor.execute(
            "SELECT id FROM masters WHERE first_name = ? AND last_name = ?",
            (first_name, last_name)
        )
    else:
        cursor.execute(
            "SELECT id FROM masters WHERE first_name = ? OR last_name = ?",
            (master_name, master_name)
        )
    
    master_result = cursor.fetchone()
    if not master_result:
        raise ValueError(f"Мастер '{master_name}' не найден")
    
    master_id = master_result[0]
    
    # Поиск услуг по названиям
    service_ids = []
    for service_title in services_list:
        cursor.execute("SELECT id FROM services WHERE title = ?", (service_title,))
        service_result = cursor.fetchone()
        if not service_result:
            raise ValueError(f"Услуга '{service_title}' не найдена")
        service_ids.append(service_result[0])
    
    # Создание записи
    cursor.execute(
        "INSERT INTO appointments (name, phone, master_id, comment) VALUES (?, ?, ?, ?)",
        (client_name, client_phone, master_id, comment)
    )
    
    appointment_id = cursor.lastrowid
    
    # Связывание записи с услугами
    for service_id in service_ids:
        cursor.execute(
            "INSERT INTO appointments_services (appointment_id, service_id) VALUES (?, ?)",
            (appointment_id, service_id)
        )
    
    conn.commit()
    return appointment_id


# Тестирование функций
if __name__ == "__main__":
    # Создание базы данных
    try:
        # Чтение и выполнение SQL-скрипта
        sql_script = read_sql_file(SQL_SCRIPT_PATH)
        
        with sqlite3.connect(DATABASE_PATH) as conn:
            execute_script(conn, sql_script)
            print("✅ База данных успешно создана и заполнена")
            
            # Тестирование поиска по телефону
            print("\n🔍 Поиск записей по телефону '+7(999)111-22-33':")
            phone_results = find_appointment_by_phone(conn, '+7(999)111-22-33')
            for result in phone_results:
                print(f"ID: {result[0]}, Клиент: {result[1]}, Мастер: {result[4]}, Услуги: {result[5]}")
            
            # Тестирование поиска по комментарию
            print("\n🔍 Поиск записей по комментарию (содержит 'клиент'):")
            comment_results = find_appointment_by_comment(conn, 'клиент')
            for result in comment_results:
                print(f"ID: {result[0]}, Клиент: {result[1]}, Комментарий: {result[7]}")
            
            # Тестирование создания новой записи
            print("\n➕ Создание новой записи:")
            try:
                new_appointment_id = create_appointment(
                    conn,
                    client_name="Владимир Тестов",
                    client_phone="+7(999)000-11-22",
                    master_name="Иван Петров",
                    services_list=["Мужская стрижка", "Стрижка бороды"],
                    comment="Тестовая запись"
                )
                print(f"✅ Создана новая запись с ID: {new_appointment_id}")
                
                # Проверка созданной записи
                verification_results = find_appointment_by_phone(conn, "+7(999)000-11-22")
                if verification_results:
                    result = verification_results[0]
                    print(f"Проверка: {result[1]} записан к {result[4]} на услуги: {result[5]}")
                
            except ValueError as e:
                print(f"❌ Ошибка при создании записи: {e}")
            
            print("\n📊 Все записи в базе данных:")
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    a.id,
                    a.name,
                    a.phone,
                    m.first_name || ' ' || m.last_name AS master_name,
                    a.status,
                    a.comment
                FROM appointments a
                LEFT JOIN masters m ON a.master_id = m.id
                ORDER BY a.id
            """)
            all_appointments = cursor.fetchall()
            for appointment in all_appointments:
                print(f"ID: {appointment[0]}, {appointment[1]} ({appointment[2]}) -> {appointment[3]}, Статус: {appointment[4]}")
                
    except FileNotFoundError:
        print(f"❌ Файл {SQL_SCRIPT_PATH} не найден")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
