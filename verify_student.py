import sqlite3

def verify_student():
    try:
        connection = sqlite3.connect(r"D:\dataBaseProject\db\student_info_system.db")
        cursor = connection.cursor()
        
        cursor.execute('''
            SELECT Name FROM Students WHERE StudentID = 5506104
        ''')
        
        result = cursor.fetchone()
        
        if result:
            print(f"StudentID 5506104 corresponds to: {result[0]}")
        else:
            print("No student found with StudentID 5506104")
        
    except sqlite3.DatabaseError as e:
        print(e)
    
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    verify_student()
