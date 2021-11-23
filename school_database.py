import sqlite3

student_conn = sqlite3.connect('Lists/students.db')
student_cursor = student_conn.cursor()

student_cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                        fname text,
                        lname text,
                        major text,
                        grad_year text,
                        gpa text,
                        email text
                        )""")


faculty_conn = sqlite3.connect('Lists/faculty.db')
faculty_cursor = faculty_conn.cursor()

faculty_cursor.execute("""CREATE TABLE IF NOT EXISTS faculty(
                        fname text,
                        lname text,
                        dept text,
                        start_date text,
                        is_adjunct text,
                        is_tenured text,
                        salary text,
                        email text
                        )""")


staff_conn = sqlite3.connect('Lists/staff.db')
staff_cursor = staff_conn.cursor()

staff_cursor.execute("""CREATE TABLE IF NOT EXISTS staff(
                        fname text,
                        lname text,
                        dept text,
                        start_date text,
                        position text,
                        salary text,
                        email text
                        )""")


def insert_to_database(x, info):
    if x == "student":
        student_cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)", info)
        student_conn.commit()
    elif x == "faculty":
        faculty_cursor.execute("INSERT INTO faculty VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info)
        faculty_conn.commit()
    elif x == "staff":
        staff_cursor.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?, ?)", info)
        staff_conn.commit()


def fetch(x):
    if x == "student":
        student_cursor.execute("SELECT * FROM students")
        s = student_cursor.fetchall()
        return s
    elif x == "faculty":
        faculty_cursor.execute("SELECT * FROM faculty")
        f = faculty_cursor.fetchall()
        return f
    elif x == "staff":
        staff_cursor.execute("SELECT * FROM staff")
        st = staff_cursor.fetchall()
        return st

