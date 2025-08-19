from db_connection import conn, cursor


querie = {
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
        HAVING COUNT(DISTINCT students.sex) > 1"""
    }


class Execute:
    def __init__(self):
        self.querie = querie
        self.conn = conn
        self.cursor = cursor

    def first_querie(self):
        self.cursor.execute(self.querie[1])
        result1 = self.cursor.fetchall()
        for room, age in result1:
            print(f"{room}  {age}")

    def second_querie(self):
        self.cursor.execute(self.querie[2])
        result2 = self.cursor.fetchall()
        for a, b in result2:
            print(f"{a}  {b}")

    def third_querie(self):
        self.cursor.execute(self.querie[3])
        result3 = self.cursor.fetchall()
        for a, b in result3:
            print(f"{a}  {b}")

    def forth_querie(self):
        self.cursor.execute(self.querie[4])
        result4 = self.cursor.fetchall()
        for a, b in result4:
            print(f"{a}  {b} ")
