from db_connection import conn, cursor


queries = {
    1: """Select 
            rooms.name, 
            Count(*) 
        From rooms 
        join students on rooms.id = students.room
        group by rooms.name
        order by count """,
    2: """SELECT 
            rooms.id,
            AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, students.birthday))) AS avg_age
        FROM rooms 
        JOIN students ON rooms.id = students.room
        GROUP BY rooms.id
        ORDER BY avg_age
        LIMIT 5 """,
    3: """select room, 
            MAX(EXTRACT(YEAR FROM AGE(CURRENT_DATE, students.birthday))) -
            MIN(EXTRACT(YEAR FROM AGE(CURRENT_DATE, students.birthday))) as difference from students
        Group by room
        order by difference
        limit 5 """,
    4: """SELECT
            rooms.id,
            rooms.name
        FROM rooms
        INNER JOIN students on rooms.id = students.room
        GROUP BY rooms.id, rooms.name
        HAVING COUNT(DISTINCT students.sex) > 1""",
}


class SqlExecuter:
    def __init__(self):
        self.queries = queries
        self.conn = conn
        self.cursor = cursor

    def students_count_in_rooms(self):
        self.cursor.execute(self.queries[1])
        result1 = self.cursor.fetchall()
        for room, count in result1:
            print(f"{room}  {count}")

    def rooms_with_min_age(self):
        self.cursor.execute(self.queries[2])
        result2 = self.cursor.fetchall()
        for room_id, avg in result2:
            print(f"{room_id}  {avg}")

    def rooms_with_max_age_diff(self):
        self.cursor.execute(self.queries[3])
        result3 = self.cursor.fetchall()
        for room, diff in result3:
            print(f"{room}  {diff}")

    def m_and_f_rooms(self):
        self.cursor.execute(self.queries[4])
        result4 = self.cursor.fetchall()
        for room_id, room in result4:
            print(f"{room_id}  {room} ")
