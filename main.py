from load_data import RoomLoader, StudentLoader
from queries import SqlExecuter, create_indexes


def main():
    room_loader = RoomLoader()
    student_loader = StudentLoader()

    print("Вызов метода load_data для загрузки данных в бд")
    room_loader.load_data("data/rooms.json")
    student_loader.load_data("data/students.json")
    print("Данные загружены в бд")

    print("Выполнение запросов")
    create_indexes()
    executor = SqlExecuter()

    executor.students_count_in_rooms()
    executor.rooms_with_min_age()
    executor.rooms_with_max_age_diff()
    executor.male_rooms()
    executor.female_rooms()

if __name__ == "__main__":
    main()
