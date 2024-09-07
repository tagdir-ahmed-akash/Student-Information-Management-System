import sqlite3

def change_teacher_id(course_id, new_teacher_id, course_name):
    connection = sqlite3.connect('db/student_info_system.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    UPDATE Courses
    SET TeacherID = ?
    WHERE CourseID = ? AND CourseName = ?
    ''', (new_teacher_id, course_id, course_name))
    
    connection.commit()
    connection.close()
