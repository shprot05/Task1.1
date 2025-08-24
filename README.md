# Первый способ запуска

# 1. Клонируй репозиторий
git clone https://github.com/shprot05/Task1.1.git
cd Task1.1

# 2. Собери и запусти контейнер
docker-compose up --build


# Второй способ запуска
# 1. Клонируй репозиторий
git clone https://github.com/shprot05/Task1.1.git
cd student-room-analyzer

# 2. Установи зависимости
pip install -r requirements.txt

# 3. Настрой файл окружения .env
# Пример содержимого .env:
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database

# 4. Подготовь JSON-файлы с данными


# 5. Запусти программу
python main.py

# 6. Следуй инструкциям в консоли:
# - Введи путь к файлу студентов
# - Введи путь к файлу комнат
# - Выбери формат экспорта (json или xml)
# - Укажи путь для сохранения результатов

# 7. Результаты будут сохранены в:
# - ./json_output/ или ./xml_output/
