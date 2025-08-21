from db_connection import get_connection
import json


def create_indexes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_student_room_id ON students(room);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_student_birthday ON students(birthday);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_student_sex ON students(sex);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_room_name ON rooms(name);")
    conn.commit()



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
        output = []
        for room, count in result1:
            output.append({
                "room": room,
                "count": round(count, 2)
            })

        with open('output/students_count_in_rooms.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)

    def rooms_with_min_age(self):
        self.cursor.execute(self.queries[2])
        result2 = self.cursor.fetchall()
        output = []
        for room_name, avg in result2:
            output.append({
                "room_name": room_name,
                "min_avg": round(float(avg), 2)
            })

        with open('output/rooms_with_min_age.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)

    def rooms_with_max_age_diff(self):
        self.cursor.execute(self.queries[3])
        result3 = self.cursor.fetchall()
        output = []
        for room, diff in result3:
            output.append({
                "room": room,
                "diff": round((float(diff)), 2)
            })

            with open('output/rooms_with_max_age_diff.json', 'w', encoding='utf-8') as f:
                json.dump(output, f, ensure_ascii=False, indent=4)

    def male_rooms(self):
        self.cursor.execute(self.queries[4])
        result4 = self.cursor.fetchall()
        rooms = [room_name[0] for room_name in result4]  # вытягиваем строку из кортежа

        with open('output/male_rooms.json', 'w', encoding='utf-8') as f:
            json.dump(rooms, f, ensure_ascii=False, indent=4)

    def female_rooms(self):
        self.cursor.execute(self.queries[5])
        result4 = self.cursor.fetchall()
        rooms = [room_name[0] for room_name in result4]

        with open('output/female_rooms.json', 'w', encoding='utf-8') as f:
            json.dump(rooms, f, ensure_ascii=False, indent=4)
