from load_data import RoomLoader, StudentLoader
from queries import SqlExecuter


def main():
    room_loader = RoomLoader()
    student_loader = StudentLoader()
    room_loader.load_data("C:\\Users\\37529\\Downloads\\rooms.json")
    student_loader.load_data("C:\\Users\\37529\\Downloads\\students.json")

    executor = SqlExecuter()

    executor.students_count_in_rooms()
    # executor.rooms_with_min_age()
    # executor.rooms_with_max_age_diff()
    # executor.m_and_f_rooms()


if __name__ == "__main__":
    main()
