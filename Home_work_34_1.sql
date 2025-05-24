-- Отключение проверки внешних ключей
PRAGMA foreign_keys = OFF;

-- Начало транзакции
BEGIN TRANSACTION;

-- Удаление существующих таблиц (если есть)
DROP TABLE IF EXISTS appointments_services;
DROP TABLE IF EXISTS masters_services;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS masters;

-- Создание таблицы "Мастера"
CREATE TABLE masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone TEXT NOT NULL UNIQUE
);

-- Создание таблицы "Услуги"
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT,
    price REAL NOT NULL CHECK (price > 0)
);

-- Создание таблицы "Запись на услуги"
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER,
    status TEXT DEFAULT 'ожидает' CHECK (status IN ('ожидает', 'подтверждена', 'отменена', 'завершена')),
    comment TEXT,
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE SET NULL
);

-- Создание связующей таблицы между мастерами и услугами
CREATE TABLE masters_services (
    master_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (master_id, service_id),
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Создание связующей таблицы между записями и услугами
CREATE TABLE appointments_services (
    appointment_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Добавление данных о мастерах
INSERT INTO masters (first_name, last_name, middle_name, phone) VALUES
    ('Иван', 'Петров', 'Сергеевич', '+7(999)123-45-67'),
    ('Алексей', 'Иванов', 'Дмитриевич', '+7(999)987-65-43'),
    ('Дмитрий', 'Сидоров', 'Александрович', '+7(999)555-66-77');

-- Добавление услуг
INSERT INTO services (title, description, price) VALUES
    ('Мужская стрижка', 'Классическая мужская стрижка', 1200.00),
    ('Стрижка бороды', 'Моделирование и стрижка бороды', 800.00),
    ('Бритье опасной бритвой', 'Традиционное бритье с использованием опасной бритвы', 1000.00),
    ('Детская стрижка', 'Стрижка для мальчиков до 12 лет', 800.00),
    ('Комплекс (стрижка + борода)', 'Комплексная услуга включающая стрижку и оформление бороды', 1800.00),
    ('Укладка волос', 'Профессиональная укладка волос', 600.00);

-- Связывание мастеров и услуг
INSERT INTO masters_services (master_id, service_id) VALUES
    (1, 1), (1, 2), (1, 5),
    (2, 1), (2, 3), (2, 4),
    (3, 1), (3, 2), (3, 6);

-- Добавление записей на услуги
INSERT INTO appointments (name, phone, master_id, status, comment) VALUES
    ('Сергей Сидоров', '+7(999)111-22-33', 1, 'подтверждена', 'Постоянный клиент'),
    ('Дмитрий Козлов', '+7(999)222-33-44', 2, 'ожидает', 'Первое посещение'),
    ('Андрей Смирнов', '+7(999)333-44-55', 1, 'подтверждена', 'Срочная запись'),
    ('Михаил Соколов', '+7(999)444-55-66', 2, 'завершена', 'Регулярный клиент'),
    ('Петр Васильев', '+7(999)777-88-99', 3, 'ожидает', 'Особые пожелания по стрижке');

-- Связывание записей и услуг
INSERT INTO appointments_services (appointment_id, service_id) VALUES
    (1, 1), (2, 3), (2, 1), (3, 5), (4, 4), (5, 1), (5, 6);

-- Создание индексов
-- Индекс по телефону клиента - ускоряет поиск записей по номеру телефона
CREATE INDEX idx_appointments_phone ON appointments(phone);

-- Индекс по статусу записи - ускоряет фильтрацию записей по статусу
CREATE INDEX idx_appointments_status ON appointments(status);

-- Составной индекс по мастеру и дате - ускоряет поиск записей конкретного мастера за определенный период
CREATE INDEX idx_appointments_master_date ON appointments(master_id, date);

-- Составной индекс по имени и фамилии мастера - ускоряет поиск мастеров по ФИО
CREATE INDEX idx_masters_name ON masters(first_name, last_name);

-- Завершение транзакции
COMMIT;

-- Включение проверки внешних ключей
PRAGMA foreign_keys = ON;
