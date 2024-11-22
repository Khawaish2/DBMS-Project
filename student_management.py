import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk, messagebox



# Database Connection
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Change this to your MySQL server
            user="root",  # Your MySQL username
            password="Khawaish@123",  # Your MySQL password
            database="StudentManagement"  # Your database name
        )
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None


# Add Student
def add_student():
    def save_student():
        name = name_entry.get()
        age = age_entry.get()
        address = address_entry.get()
        if not name or not age or not address:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO Students (Name, Age, Address) VALUES (%s, %s, %s)"
                data = (name, age, address)
                cursor.execute(query, data)
                connection.commit()
                messagebox.showinfo("Success", "Student added successfully!")
                add_window.destroy()
            except Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                connection.close()

    add_window = tk.Toplevel()
    add_window.title("Add Student")

    tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Age:").grid(row=1, column=0, padx=10, pady=10)
    age_entry = tk.Entry(add_window)
    age_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Address:").grid(row=2, column=0, padx=10, pady=10)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(add_window, text="Save", command=save_student).grid(row=3, column=0, columnspan=2, pady=10)


# View Students
def view_students():
    view_window = tk.Toplevel()
    view_window.title("View Students")
    view_window.geometry("500x300")

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Students")
            records = cursor.fetchall()

            columns = ("StudentID", "Name", "Age", "Address")
            tree = ttk.Treeview(view_window, columns=columns, show="headings")
            tree.heading("StudentID", text="ID")
            tree.heading("Name", text="Name")
            tree.heading("Age", text="Age")
            tree.heading("Address", text="Address")

            for record in records:
                tree.insert("", tk.END, values=record)

            tree.pack(fill=tk.BOTH, expand=True)
        except Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            connection.close()


# Delete Student
def delete_student():
    def delete_by_id():
        student_id = id_entry.get()
        if not student_id:
            messagebox.showerror("Input Error", "Student ID is required!")
            return

        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM Students WHERE StudentID = %s"
                cursor.execute(query, (student_id,))
                connection.commit()
                if cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Student deleted successfully!")
                    delete_window.destroy()
                else:
                    messagebox.showerror("Error", "Student ID not found!")
            except Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                connection.close()

    delete_window = tk.Toplevel()
    delete_window.title("Delete Student")

    tk.Label(delete_window, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(delete_window, text="Delete", command=delete_by_id).grid(row=1, column=0, columnspan=2, pady=10)


def add_course():
    def save_course():
        name = name_entry.get()
        duration = duration_entry.get()
        credits = credits_entry.get()
        if not name or not duration or not credits:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO Courses (CourseName, Duration, Credits) VALUES (%s, %s, %s)"
                data = (name, duration, credits)
                cursor.execute(query, data)
                connection.commit()
                messagebox.showinfo("Success", "Course added successfully!")
                add_window.destroy()
            except Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                connection.close()

    add_window = tk.Toplevel()
    add_window.title("Add Course")

    tk.Label(add_window, text="Course Name:").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Duration:").grid(row=1, column=0, padx=10, pady=10)
    duration_entry = tk.Entry(add_window)
    duration_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Credits:").grid(row=2, column=0, padx=10, pady=10)
    credits_entry = tk.Entry(add_window)
    credits_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(add_window, text="Save", command=save_course).grid(row=3, column=0, columnspan=2, pady=10)


def view_courses():
    view_window = tk.Toplevel()
    view_window.title("View Courses")
    view_window.geometry("500x300")

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Courses")
            records = cursor.fetchall()

            columns = ("CourseID", "CourseName", "Duration", "Credits")
            tree = ttk.Treeview(view_window, columns=columns, show="headings")
            tree.heading("CourseID", text="ID")
            tree.heading("CourseName", text="Name")
            tree.heading("Duration", text="Duration")
            tree.heading("Credits", text="Credits")

            for record in records:
                tree.insert("", tk.END, values=record)

            tree.pack(fill=tk.BOTH, expand=True)
        except Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            connection.close()


def enroll_student():
    def save_enrollment():
        student_id = student_id_entry.get()
        course_id = course_id_entry.get()
        if not student_id or not course_id:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO Enrollments (StudentID, CourseID) VALUES (%s, %s)"
                data = (student_id, course_id)
                cursor.execute(query, data)
                connection.commit()
                messagebox.showinfo("Success", "Student enrolled successfully!")
                enroll_window.destroy()
            except Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                connection.close()

    enroll_window = tk.Toplevel()
    enroll_window.title("Enroll Student")

    tk.Label(enroll_window, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
    student_id_entry = tk.Entry(enroll_window)
    student_id_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(enroll_window, text="Course ID:").grid(row=1, column=0, padx=10, pady=10)
    course_id_entry = tk.Entry(enroll_window)
    course_id_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(enroll_window, text="Enroll", command=save_enrollment).grid(row=2, column=0, columnspan=2, pady=10)


def add_marks():
    def save_marks():
        student_id = student_id_entry.get()
        course_id = course_id_entry.get()
        marks = marks_entry.get()
        if not student_id or not course_id or not marks:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO Marks (StudentID, CourseID, Marks) VALUES (%s, %s, %s)"
                data = (student_id, course_id, marks)
                cursor.execute(query, data)
                connection.commit()
                messagebox.showinfo("Success", "Marks added successfully!")
                add_window.destroy()
            except Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                connection.close()

    add_window = tk.Toplevel()
    add_window.title("Add Marks")

    tk.Label(add_window, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
    student_id_entry = tk.Entry(add_window)
    student_id_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Course ID:").grid(row=1, column=0, padx=10, pady=10)
    course_id_entry = tk.Entry(add_window)
    course_id_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Marks:").grid(row=2, column=0, padx=10, pady=10)
    marks_entry = tk.Entry(add_window)
    marks_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(add_window, text="Save", command=save_marks).grid(row=3, column=0, columnspan=2, pady=10)


# Main GUI
def main_gui():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("600x400")

    # Buttons for Students
    tk.Label(root, text="Student Management", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Add Student", command=add_student, width=20).pack(pady=5)
    tk.Button(root, text="View Students", command=view_students, width=20).pack(pady=5)
    tk.Button(root, text="Delete Student", command=delete_student, width=20).pack(pady=5)

    # Buttons for Courses
    tk.Label(root, text="Course Management", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Add Course", command=add_course, width=20).pack(pady=5)
    tk.Button(root, text="View Courses", command=view_courses, width=20).pack(pady=5)

    # Buttons for Enrollments
    tk.Label(root, text="Enrollment Management", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Enroll Student", command=enroll_student, width=20).pack(pady=5)

    # Buttons for Marks
    tk.Label(root, text="Marks Management", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Add Marks", command=add_marks, width=20).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_gui()
