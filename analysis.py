
import sqlite3
conn = sqlite3.connect('db/student_info_system.db')
cursor = conn.cursor()

def studentNumber():
    cursor.execute('''
    select count(*) from Students
    ''')
    numbers = cursor.fetchall()
    for number in numbers:
     print(number)
studentNumber()  

def studentCountByYear():
    cursor.execute('''
    SELECT EnrollmentYear, COUNT(*) 
    FROM Students 
    GROUP BY EnrollmentYear
    ''')
    results = cursor.fetchall()
    for result in results:
        print(result)
studentCountByYear()

def courseCountByTeacher():
    cursor.execute('''
    SELECT Teachers.TeacherID, Teachers.Name, COUNT(*) 
    FROM Teachers
    JOIN TeacherCourse ON Teachers.TeacherID = TeacherCourse.TeacherID
    GROUP BY Teachers.TeacherID, Teachers.Name
    ''')
    results = cursor.fetchall()
    for result in results:
        print(result)
courseCountByTeacher()

def coursesWithTeachers():
    cursor.execute('''
    SELECT Courses.CourseID, Courses.CourseName, Teachers.Name 
    FROM Courses
    JOIN TeacherCourse ON Courses.CourseID = TeacherCourse.CourseID
    JOIN Teachers ON TeacherCourse.TeacherID = Teachers.TeacherID
    ''')
    results = cursor.fetchall()
    for result in results:
        print(result)
coursesWithTeachers()

def bookCountByCourse():
    cursor.execute('''
    SELECT Courses.CourseID, Courses.CourseName, COUNT(*) 
    FROM Courses
    JOIN CourseBooks ON Courses.CourseID = CourseBooks.CourseID
    GROUP BY Courses.CourseID, Courses.CourseName
    ''')
    results = cursor.fetchall()
    for result in results:
        print(result)
bookCountByCourse()

def teachersWithManyCourses(minCourses):
    cursor.execute('''
    SELECT Teachers.TeacherID, Teachers.Name, COUNT(*) AS CourseCount
    FROM Teachers
    JOIN TeacherCourse ON Teachers.TeacherID = TeacherCourse.TeacherID
    GROUP BY Teachers.TeacherID, Teachers.Name
    HAVING CourseCount > ?
    ''', (minCourses,))
    results = cursor.fetchall()
    for result in results:
        print(result)
teachersWithManyCourses(3)

def mostCommonStudentMajor():
    cursor.execute('''
    SELECT Major, COUNT(*) AS MajorCount
    FROM Students
    GROUP BY Major
    ORDER BY MajorCount DESC
    LIMIT 1
    ''')
    result = cursor.fetchone()
    print(result)
mostCommonStudentMajor()

def averageCoursesPerTeacher():
    cursor.execute('''
    SELECT AVG(CourseCount) 
    FROM (
        SELECT Teachers.TeacherID, COUNT(*) AS CourseCount
        FROM Teachers
        JOIN TeacherCourse ON Teachers.TeacherID = TeacherCourse.TeacherID
        GROUP BY Teachers.TeacherID
    ) AS TeacherCourseCounts
    ''')
    result = cursor.fetchone()
    print(result)
averageCoursesPerTeacher()


conn.commit()
conn.close()
