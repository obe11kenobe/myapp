-- Создание таблицы employees
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INTEGER NOT NULL,
    position VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL
);

-- Вставка тестовых данных
INSERT INTO employees (full_name, gender, age, position, category)
VALUES
    ('Иванов Иван Иванович', 'Мужской', 30, 'Разработчик', 'Senior'),
    ('Петрова Анна Сергеевна', 'Женский', 25, 'Дизайнер', 'Middle');