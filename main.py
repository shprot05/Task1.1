from load_data import RoomLoader, StudentLoader
from queries import SqlExecuter, create_indexes


def main():
    room_loader = RoomLoader()
    student_loader = StudentLoader()
    room_loader.load_data("data/rooms.json")
    student_loader.load_data("data/students.json")

    create_indexes()
    executor = SqlExecuter()

    executor.students_count_in_rooms()
    executor.rooms_with_min_age()
    executor.rooms_with_max_age_diff()
    executor.male_rooms()
    executor.female_rooms()

if __name__ == "__main__":
    main()
