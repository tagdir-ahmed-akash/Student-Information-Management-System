import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function definitions
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

def update_student(cursor, student_id, new_name, new_enrollment_year, new_major, new_gender):
    cursor.execute('''
    UPDATE Students
    SET Name = ?, EnrollmentYear = ?, Major = ?, Gender = ?
    WHERE StudentID = ?
    ''', (new_name, new_enrollment_year, new_major, new_gender, student_id))

def delete_student(cursor, student_id):
    cursor.execute('''
    DELETE FROM Students
    WHERE StudentID = ?
    ''', (student_id,))

def search_teacher(cursor, teacher_id):
    cursor.execute('''
    SELECT * FROM Teachers WHERE TeacherID = ?
    ''', (teacher_id,))
    return cursor.fetchone()

# Function to handle button clicks for creating a student
def handle_create_student():
    try:
        student_id = int(student_id_entry.get())
        name = name_entry.get()
        enrollment_year = int(enrollment_year_entry.get())
        major = major_entry.get()
        gender = gender_entry.get()

        create_student(cursor, student_id, name, enrollment_year, major, gender)
        conn.commit()
        messagebox.showinfo("Success", f"Student {student_id} created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to handle button clicks for deleting a student
def handle_delete_student():
    try:
        student_id = int(student_id_entry_delete.get())

        delete_student(cursor, student_id)
        conn.commit()
        messagebox.showinfo("Success", f"Student {student_id} deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to handle button clicks for updating a student
def handle_update_student():
    try:
        student_id = int(student_id_entry_update.get())
        new_name = name_entry_update.get()
        new_enrollment_year = int(enrollment_year_entry_update.get())
        new_major = major_entry_update.get()
        new_gender = gender_entry_update.get()

        update_student(cursor, student_id, new_name, new_enrollment_year, new_major, new_gender)
        conn.commit()
        messagebox.showinfo("Success", f"Student {student_id} information updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to handle button clicks for creating a course
def handle_create_course():
    try:
        course_id = int(course_id_entry.get())
        course_name = course_name_entry.get()
        teacher_id = int(teacher_id_entry.get())

        create_course(cursor, course_id, course_name, teacher_id)
        conn.commit()
        messagebox.showinfo("Success", f"Course {course_id} created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to handle button clicks for creating a book
def handle_create_book():
    try:
        book_id = int(book_id_entry.get())
        title = title_entry.get()
        major = major_entry.get()

        create_book(cursor, book_id, title, major)
        conn.commit()
        messagebox.showinfo("Success", f"Book {book_id} created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to handle button clicks for assigning a book to a course
def handle_assign_book_to_course():
    try:
        course_id = int(course_id_entry2.get())
        book_id = int(book_id_entry2.get())

        assign_book_to_course(cursor, course_id, book_id)
        conn.commit()
        messagebox.showinfo("Success", f"Book {book_id} assigned to Course {course_id} successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to handle button clicks for searching a teacher
def handle_search_teacher():
    try:
        teacher_id = int(teacher_id_entry_search.get())

        teacher_info = search_teacher(cursor, teacher_id)
        if teacher_info:
            teacher_info_label.config(text=f"Teacher ID: {teacher_info[0]}, Name: {teacher_info[1]}, Department: {teacher_info[2]}")
        else:
            teacher_info_label.config(text="Teacher not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Initialize Tkinter window
root = tk.Tk()
root.title("University Management System")
root.configure(bg='black')

# Connect to SQLite database
conn = sqlite3.connect('db/student_info_system.db')
cursor = conn.cursor()

# Create frames for grouping related widgets

# Main frame for the whole interface
main_frame = tk.Frame(root, bg='black')
main_frame.pack(fill=tk.BOTH, expand=True)

# Frame for student management on the left
student_frame = tk.LabelFrame(main_frame, text="Student Management", padx=10, pady=10, bg='black', fg='white', font=("Arial", 12, "bold"))
student_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Frame for course management on the right
course_frame = tk.LabelFrame(main_frame, text="Course Management", padx=10, pady=10, bg='black', fg='white', font=("Arial", 12, "bold"))
course_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# Frame for book management on the left (below student management)
book_frame = tk.LabelFrame(main_frame, text="Book Management", padx=10, pady=10, bg='black', fg='white', font=("Arial", 12, "bold"))
book_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Frame for assignments on the right (below course management)
assignment_frame = tk.LabelFrame(main_frame, text="Assignments", padx=10, pady=10, bg='black', fg='white', font=("Arial", 12, "bold"))
assignment_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

# Frame for search functionality at the bottom
search_frame = tk.LabelFrame(root, text="Search", padx=10, pady=10, bg='black', fg='white', font=("Arial", 12, "bold"))
search_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Common style settings for labels and entry fields
label_style = {'bg': 'black', 'fg': 'white'}
entry_style = {'bg': 'black', 'fg': 'white', 'insertbackground': 'white'}

# Student Management Widgets
tk.Label(student_frame, text="Student ID:", **label_style).grid(row=0, column=0, padx=5, pady=5)
student_id_entry = tk.Entry(student_frame, **entry_style)
student_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(student_frame, text="Name:", **label_style).grid(row=0, column=2, padx=5, pady=5)
name_entry = tk.Entry(student_frame, **entry_style)
name_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(student_frame, text="Enrollment Year:", **label_style).grid(row=1, column=0, padx=5, pady=5)
enrollment_year_entry = tk.Entry(student_frame, **entry_style)
enrollment_year_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(student_frame, text="Major:", **label_style).grid(row=1, column=2, padx=5, pady=5)
major_entry = tk.Entry(student_frame, **entry_style)
major_entry.grid(row=1, column=3, padx=5, pady=5)

tk.Label(student_frame, text="Gender:", **label_style).grid(row=2, column=0, padx=5, pady=5)
gender_entry = tk.Entry(student_frame, **entry_style)
gender_entry.grid(row=2, column=1, padx=5, pady=5)

create_student_button = tk.Button(student_frame, text="Create Student", command=handle_create_student, bg='#4CAF50', fg='white', font=("Arial", 10, "bold"))
create_student_button.grid(row=3, column=0, columnspan=2, pady=5, sticky='ew')

tk.Label(student_frame, text="Student ID to Delete:", **label_style).grid(row=4, column=0, padx=5, pady=5)
student_id_entry_delete = tk.Entry(student_frame, **entry_style)
student_id_entry_delete.grid(row=4, column=1, padx=5, pady=5)

delete_student_button = tk.Button(student_frame, text="Delete Student", command=handle_delete_student, bg='#FF5733', fg='white', font=("Arial", 10, "bold"))
delete_student_button.grid(row=5, column=0, columnspan=2, pady=5, sticky='ew')

tk.Label(student_frame, text="Student ID to Update:", **label_style).grid(row=6, column=0, padx=5, pady=5)
student_id_entry_update = tk.Entry(student_frame, **entry_style)
student_id_entry_update.grid(row=6, column=1, padx=5, pady=5)

tk.Label(student_frame, text="New Name:", **label_style).grid(row=7, column=0, padx=5, pady=5)
name_entry_update = tk.Entry(student_frame, **entry_style)
name_entry_update.grid(row=7, column=1, padx=5, pady=5)

tk.Label(student_frame, text="New Enrollment Year:", **label_style).grid(row=8, column=0, padx=5, pady=5)
enrollment_year_entry_update = tk.Entry(student_frame, **entry_style)
enrollment_year_entry_update.grid(row=8, column=1, padx=5, pady=5)

tk.Label(student_frame, text="New Major:", **label_style).grid(row=9, column=0, padx=5, pady=5)
major_entry_update = tk.Entry(student_frame, **entry_style)
major_entry_update.grid(row=9, column=1, padx=5, pady=5)

tk.Label(student_frame, text="New Gender:", **label_style).grid(row=10, column=0, padx=5, pady=5)
gender_entry_update = tk.Entry(student_frame, **entry_style)
gender_entry_update.grid(row=10, column=1, padx=5, pady=5)

update_student_button = tk.Button(student_frame, text="Update Student", command=handle_update_student, bg='#1976D2', fg='white', font=("Arial", 10, "bold"))
update_student_button.grid(row=11, column=0, columnspan=2, pady=5, sticky='ew')

# Course Management Widgets
tk.Label(course_frame, text="Course ID:", **label_style).grid(row=0, column=0, padx=5, pady=5)
course_id_entry = tk.Entry(course_frame, **entry_style)
course_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(course_frame, text="Course Name:", **label_style).grid(row=0, column=2, padx=5, pady=5)
course_name_entry = tk.Entry(course_frame, **entry_style)
course_name_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(course_frame, text="Teacher ID:", **label_style).grid(row=1, column=0, padx=5, pady=5)
teacher_id_entry = tk.Entry(course_frame, **entry_style)
teacher_id_entry.grid(row=1, column=1, padx=5, pady=5)

create_course_button = tk.Button(course_frame, text="Create Course", command=handle_create_course, bg='#4CAF50', fg='white', font=("Arial", 10, "bold"))
create_course_button.grid(row=2, column=0, columnspan=2, pady=5, sticky='ew')

# Book Management Widgets
tk.Label(book_frame, text="Book ID:", **label_style).grid(row=0, column=0, padx=5, pady=5)
book_id_entry = tk.Entry(book_frame, **entry_style)
book_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(book_frame, text="Title:", **label_style).grid(row=0, column=2, padx=5, pady=5)
title_entry = tk.Entry(book_frame, **entry_style)
title_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(book_frame, text="Major:", **label_style).grid(row=1, column=0, padx=5, pady=5)
major_entry = tk.Entry(book_frame, **entry_style)
major_entry.grid(row=1, column=1, padx=5, pady=5)

create_book_button = tk.Button(book_frame, text="Create Book", command=handle_create_book, bg='#4CAF50', fg='white', font=("Arial", 10, "bold"))
create_book_button.grid(row=2, column=0, columnspan=2, pady=5, sticky='ew')

# Assignments Widgets
tk.Label(assignment_frame, text="Course ID:", **label_style).grid(row=0, column=0, padx=5, pady=5)
course_id_entry2 = tk.Entry(assignment_frame, **entry_style)
course_id_entry2.grid(row=0, column=1, padx=5, pady=5)

tk.Label(assignment_frame, text="Book ID:", **label_style).grid(row=0, column=2, padx=5, pady=5)
book_id_entry2 = tk.Entry(assignment_frame, **entry_style)
book_id_entry2.grid(row=0, column=3, padx=5, pady=5)

assign_book_button = tk.Button(assignment_frame, text="Assign Book to Course", command=handle_assign_book_to_course, bg='#1976D2', fg='white', font=("Arial", 10, "bold"))
assign_book_button.grid(row=1, column=0, columnspan=2, pady=5, sticky='ew')

# Search Widgets
tk.Label(search_frame, text="Teacher ID to Search:", **label_style).pack(side=tk.LEFT, padx=5, pady=5)
teacher_id_entry_search = tk.Entry(search_frame, **entry_style)
teacher_id_entry_search.pack(side=tk.LEFT, padx=5, pady=5)

search_teacher_button = tk.Button(search_frame, text="Search Teacher", command=handle_search_teacher, bg='#FFC107', fg='white', font=("Arial", 10, "bold"))
search_teacher_button.pack(side=tk.LEFT, padx=5, pady=5)

teacher_info_label = tk.Label(search_frame, **label_style)
teacher_info_label.pack(side=tk.LEFT, padx=5, pady=5)

# Start the main loop
root.mainloop()

# Close the database connection
conn.close()