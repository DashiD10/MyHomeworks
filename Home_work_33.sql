-- Создание таблицы "Мастера"
CREATE TABLE IF NOT EXISTS masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone TEXT NOT NULL
);

-- Создание таблицы "Услуги"
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT,
    price REAL NOT NULL
);

-- Создание таблицы "Запись на услуги"
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER,
    status TEXT DEFAULT 'ожидает',
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE SET NULL
);

-- Создание связующей таблицы между мастерами и услугами
CREATE TABLE IF NOT EXISTS masters_services (
    master_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (master_id, service_id),
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Создание связующей таблицы между записями и услугами
CREATE TABLE IF NOT EXISTS appointments_services (
    appointment_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Добавление данных о мастерах
INSERT INTO masters (first_name, last_name, middle_name, phone) VALUES
    ('Иван', 'Петров', 'Сергеевич', '+7(999)123-45-67'),
    ('Алексей', 'Иванов', 'Дмитриевич', '+7(999)987-65-43');

-- Добавление услуг
INSERT INTO services (title, description, price) VALUES
    ('Мужская стрижка', 'Классическая мужская стрижка', 1200.00),
    ('Стрижка бороды', 'Моделирование и стрижка бороды', 800.00),
    ('Бритье опасной бритвой', 'Традиционное бритье с использованием опасной бритвы', 1000.00),
    ('Детская стрижка', 'Стрижка для мальчиков до 12 лет', 800.00),
    ('Комплекс (стрижка + борода)', 'Комплексная услуга включающая стрижку и оформление бороды', 1800.00);

-- Связывание мастеров и услуг
INSERT INTO masters_services (master_id, service_id) VALUES
    (1, 1), -- Иван Петров выполняет мужскую стрижку
    (1, 2), -- Иван Петров выполняет стрижку бороды
    (1, 5), -- Иван Петров выполняет комплекс
    (2, 1), -- Алексей Иванов выполняет мужскую стрижку
    (2, 3), -- Алексей Иванов выполняет бритье опасной бритвой
    (2, 4); -- Алексей Иванов выполняет детскую стрижку

-- Добавление записей на услуги
INSERT INTO appointments (name, phone, master_id, status) VALUES
    ('Сергей Сидоров', '+7(999)111-22-33', 1, 'подтверждена'),
    ('Дмитрий Козлов', '+7(999)222-33-44', 2, 'ожидает'),
    ('Андрей Смирнов', '+7(999)333-44-55', 1, 'подтверждена'),
    ('Михаил Соколов', '+7(999)444-55-66', 2, 'отменена');

-- Связывание записей и услуг
INSERT INTO appointments_services (appointment_id, service_id) VALUES
    (1, 1), -- Сергей Сидоров записался на мужскую стрижку
    (2, 3), -- Дмитрий Козлов записался на бритье опасной бритвой
    (2, 1), -- Дмитрий Козлов также записался на мужскую стрижку
    (3, 5), -- Андрей Смирнов записался на комплекс
    (4, 4); -- Михаил Соколов записался на детскую стрижку

-- Обновление статуса записи (пример обновления)
UPDATE appointments SET status = 'подтверждена' WHERE id = 2;
