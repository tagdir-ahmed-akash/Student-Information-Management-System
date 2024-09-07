import sqlite3

conn = sqlite3.connect('db/student_info_system.db')
cursor = conn.cursor()

def create_student(cursor, student_id, name, enrollment_year, major, gender):
    cursor.execute('''
    INSERT INTO Students (StudentID, Name, EnrollmentYear, Major, Gender)
    VALUES (?, ?, ?, ?, ?)
    ''', (student_id, name, enrollment_year, major, gender))

def create_course(cursor, course_id, course_name, teacher_id):
    cursor.execute('''
    INSERT INTO Courses (CourseID, CourseName, TeacherID)
    VALUES (?, ?, ?)
    ''', (course_id, course_name, teacher_id))

def create_book(cursor, book_id, title, major):
    cursor.execute('''
    INSERT INTO Books (BookID, Title, Major)
    VALUES (?, ?, ?)
    ''', (book_id, title, major))


def assign_book_to_course(cursor, course_id, book_id):
    cursor.execute('''
    INSERT INTO CourseBooks (CourseID, BookID)
    VALUES (?, ?)
    ''', (course_id, book_id))

def assign_teacher_to_course(cursor, course_id, teacher_id):
    cursor.execute('''
    INSERT INTO TeacherCourse (CourseID, TeacherID)
    VALUES (?, ?)
    ''', (course_id, teacher_id))

def update_student(cursor, student_id, new_name, new_enrollment_year, new_major, new_gender):
    cursor.execute('''
    UPDATE Students
    SET Name = ?, EnrollmentYear = ?, Major = ?, Gender = ?
    WHERE StudentID = ?
    ''', (new_name, new_enrollment_year, new_major, new_gender, student_id))

def update_teacher(cursor, teacher_id, new_name, new_dept, new_gender):
    cursor.execute('''
    UPDATE Teachers
    SET Name = ?, Dept = ?, Gender = ?
    WHERE TeacherID = ?
    ''', (new_name, new_dept, new_gender, teacher_id))

def update_course(cursor, course_id, new_course_name, new_teacher_id):
    cursor.execute('''
    UPDATE Courses
    SET CourseName = ?, TeacherID = ?
    WHERE CourseID = ?
    ''', (new_course_name, new_teacher_id, course_id))

def delete_student(cursor, student_id):
    cursor.execute('''
    DELETE FROM Students
    WHERE StudentID = ?
    ''', (student_id,))

def delete_teacher(cursor, teacher_id):
    cursor.execute('''
    DELETE FROM Teachers
    WHERE TeacherID = ?
    ''', (teacher_id,))

def delete_course(cursor, course_id):
    cursor.execute('''
    DELETE FROM Courses
    WHERE CourseID = ?
    ''', (course_id,))

def buy_book(bookID,studentID):
    cursor.execute('''
    update Students
    set OwnedBooks = ?
    where StudentID = ?
    ''',(bookID,studentID,))

def get_books():
    cursor.execute('''
    select * from Books
    ''')
    books = cursor.fetchall()
    for book in books:
        print(book)


def choose_course(student_id, course_id):
    try:
        cursor.execute('''
        INSERT INTO StudentCourse (StudentID, CourseID)
        VALUES (?, ?)
        ''', (student_id, course_id))
        conn.commit()
        print(f"Student {student_id} has enrolled in Course {course_id}.")
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")


def register_update_student(student_id, name, enrollment_year, major, gender):
    try:
        cursor.execute('''
        INSERT OR REPLACE INTO Students (StudentID, Name, EnrollmentYear, Major, Gender)
        VALUES (?, ?, ?, ?, ?)
        ''', (student_id, name, enrollment_year, major, gender))
        conn.commit()
        print(f"Student {student_id} information updated.")
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")


conn.commit()
conn.close()