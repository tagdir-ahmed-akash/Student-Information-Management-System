import sqlite3

conn = sqlite3.connect('db/student_info_system.db')
cursor = conn.cursor()


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Students (
#     StudentID INT PRIMARY KEY,
#     Name TEXT,
#     EnrollmentYear INT,
#     Major TEXT,
#     Gender TEXT,
#     )
# ''')


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Teachers (
#     TeacherID INT PRIMARY KEY,
#     Name TEXT,
#     Dept TEXT,
#     Gender TEXT
#     )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Courses(
#     CourseID INT PRIMARY KEY,
#     CourseName TEXT,
#     TeacherID INT,
#     FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
#     )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Books(
#     BookID INT PRIMARY KEY,
#     Title TEXT,
#     Major TEXT
#     )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS CourseBooks(
#     CourseID INT,
#     BookID INT,
#     PRIMARY KEY (CourseID, BookID),
#     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
#     FOREIGN KEY (BookID) REFERENCES Books(BookID)
#     )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS TeacherCourse(
#     CourseID INT,
#     TeacherID INT,
#     PRIMARY KEY (CourseID, TeacherID),
#     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
#     FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
#     )
# ''')

conn.commit()
conn.close()
