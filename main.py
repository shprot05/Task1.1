from load_data import RoomLoader, StudentLoader
from queries import SqlExecuter, create_indexes
from export_data import Exporter


# Основная функция, запускающая загрузку, обработку и экспорт данных
def main() -> None:
    room_loader = RoomLoader()
    student_loader = StudentLoader()



    # Ввод путей к JSON-файлам
    path_to_students = input("Введите путь к json файлу студентов: ")
    path_to_rooms = input("Введите путь к json файлу комнат: ")

    print("Вызов метода load_data для загрузки данных в бд")
    room_loader.load_data(path_to_rooms)
    student_loader.load_data(path_to_students)
    print("Данные загружены в бд")

    # Создание индексов для ускорения запросов
    create_indexes()

    # Ввод формата экспорта и пути
    export_format = input("В каком формате сохранить результаты? (json / xml): ").strip().lower()
    path_to_export = input("Введите путь для экспорта: ")

    print("Выполнение запросов")
    exporter = Exporter(export_format, path_to_export)
    executer = SqlExecuter(exporter)

    # Выполнение всех запросов
    executer.students_count_in_rooms()
    executer.rooms_with_min_age()
    executer.rooms_with_max_age_diff()
    executer.male_rooms()
    executer.female_rooms()

    executer.close() # закрываем соединение с бд

    print("Результаты запросов сохранены")

# Точка входа
if __name__ == "__main__":
    main()