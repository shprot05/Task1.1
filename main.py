from load_data import LoadingRooms, LoadingStudents
from queries import Execute


def main():
    room_loader = LoadingRooms()
    student_loader = LoadingStudents()
    room_loader.load_data('C:\\Users\\37529\\Downloads\\rooms.json')
    student_loader.load_data('C:\\Users\\37529\\Downloads\\students.json')

    executor = Execute()
    executor.first_querie()


if __name__ == '__main__':
    main()
