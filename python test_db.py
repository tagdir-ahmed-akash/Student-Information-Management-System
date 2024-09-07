import sqlite3

def find_stud(StudentID):
    try:
        connection = sqlite3.connect(r"D:\dataBaseProject\db\student_info_system.db")
        cursor = connection.cursor()
        
        cursor.execute('''
            SELECT Name FROM Students WHERE StudentID = ?
        ''', (StudentID,))
        
        result = cursor.fetchone()
        
        if result:
            return result[0]  # Return the name
        else:
            return None  # Return None if no student found
        
    except sqlite3.DatabaseError as e:
        print(e)
        return None  # Return None or handle the error as needed
    
    finally:
        connection.close()
