from db_connection import get_connection


queries = {
    1: """Select 
            rooms.name, 
            Count(*) 
        From rooms 
        join students on rooms.id = students.room
        group by rooms.name
        order by count""",
    2: """SELECT 
            rooms.name,
            AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, students.birthday))) AS avg_age
        FROM rooms 
        JOIN students ON rooms.id = students.room
        GROUP BY rooms.name
        ORDER BY avg_age
        LIMIT 5 """,
    3: """SELECT
            rooms.name,
            MAX(EXTRACT(YEAR FROM AGE(CURRENT_DATE, students.birthday))) -
            MIN(EXTRACT(YEAR FROM AGE(CURRENT_DATE, students.birthday))) AS age_difference
        FROM rooms
        INNER JOIN students on rooms.id = students.room
        GROUP BY rooms.id, rooms.name
        ORDER BY age_difference
        LIMIT 5 """,
    4: """SELECT
            rooms.name
        FROM rooms
        INNER JOIN students ON rooms.id = students.room
        GROUP BY rooms.id, rooms.name
        HAVING COUNT(DISTINCT students.sex) = 1
        AND MAX(students.sex) = 'M'""",
    5: """SELECT
            rooms.name
        FROM rooms
        INNER JOIN students ON rooms.id = students.room
        GROUP BY rooms.id, rooms.name
        HAVING COUNT(DISTINCT students.sex) = 1
        AND MAX(students.sex) = 'F'"""
}


class SqlExecuter:
    def __init__(self):
        self.queries = queries
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def students_count_in_rooms(self):
        self.cursor.execute(self.queries[1])
        result1 = self.cursor.fetchall()
        for room, count in result1:
            print(f"{room}  {count:2f}")

    def rooms_with_min_age(self):
        self.cursor.execute(self.queries[2])
        result2 = self.cursor.fetchall()
        for room_name, avg in result2:
            print(f"{room_name}  {avg:.2f}")

    def rooms_with_max_age_diff(self):
        self.cursor.execute(self.queries[3])
        result3 = self.cursor.fetchall()
        for room, diff in result3:
            print(f"  {room}  {diff}")

    def m_rooms(self):
        self.cursor.execute(self.queries[4])
        result4 = self.cursor.fetchall()
        for  room_name in result4:
            print(f" {room_name} ")

    def f_rooms(self):
        self.cursor.execute(self.queries[5])
        result4 = self.cursor.fetchall()
        for  room_name in result4:
            print(f" {room_name} ")
