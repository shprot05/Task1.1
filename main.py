from load_data import RoomsLoader, StudentsLoader
from queries import SqlExecuter


def main():
    room_loader = RoomsLoader()
    student_loader = StudentsLoader()
    room_loader.load_data('C:\\Users\\37529\\Downloads\\rooms.json')
    student_loader.load_data('C:\\Users\\37529\\Downloads\\students.json')

    executor = SqlExecuter()
    executor.first_querie()


if __name__ == '__main__':
    main()
