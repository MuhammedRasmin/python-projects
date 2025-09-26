import sqlite3

# ----------------- Database Setup -----------------
def create_db():
    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()

    # Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Grades table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no INTEGER,
            subject TEXT NOT NULL,
            marks INTEGER,
            FOREIGN KEY(roll_no) REFERENCES students(roll_no) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

# ----------------- Student Functions -----------------
def add_student():
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    password = input("Enter Password: ")

    try:
        conn = sqlite3.connect("system.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (roll_no, name, password))
        conn.commit()
        print("✅ Student added successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ Roll No already exists!")
    finally:
        conn.close()

def view_students():
    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- All Students ---")
    for row in rows:
        print(f"Roll No: {row[0]}, Name: {row[1]}")
    conn.close()

def update_student():
    roll_no = int(input("Enter Roll No to Update: "))
    new_name = input("Enter New Name: ")
    new_password = input("Enter New Password: ")

    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, password=? WHERE roll_no=?",
                   (new_name, new_password, roll_no))
    if cursor.rowcount == 0:
        print("⚠️ Student not found!")
    else:
        print("✅ Student updated successfully!")
    conn.commit()
    conn.close()

def delete_student():
    roll_no = int(input("Enter Roll No to Delete: "))
    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    if cursor.rowcount == 0:
        print("⚠️ Student not found!")
    else:
        print("✅ Student deleted successfully!")
    conn.commit()
    conn.close()

# ----------------- Marks Functions -----------------
def add_marks():
    roll_no = int(input("Enter Student Roll No: "))
    subject = input("Enter Subject: ")
    marks = int(input("Enter Marks: "))

    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (roll_no, subject, marks) VALUES (?, ?, ?)",
                   (roll_no, subject, marks))
    conn.commit()
    print("✅ Marks added successfully!")
    conn.close()

def update_marks():
    roll_no = int(input("Enter Student Roll No: "))
    subject = input("Enter Subject: ")
    new_marks = int(input("Enter New Marks: "))

    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE grades SET marks=? WHERE roll_no=? AND subject=?",
                   (new_marks, roll_no, subject))
    if cursor.rowcount == 0:
        print("⚠️ Record not found!")
    else:
        print("✅ Marks updated successfully!")
    conn.commit()
    conn.close()

def view_marks():
    roll_no = int(input("Enter Student Roll No: "))
    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, marks FROM grades WHERE roll_no=?", (roll_no,))
    rows = cursor.fetchall()
    if not rows:
        print("⚠️ No marks found!")
    else:
        print(f"\n--- Marks for Roll No {roll_no} ---")
        for row in rows:
            print(f"Subject: {row[0]}, Marks: {row[1]}")
    conn.close()

# ----------------- Student Login -----------------
def student_login():
    roll_no = int(input("Enter Roll No: "))
    password = input("Enter Password: ")

    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no=? AND password=?",
                   (roll_no, password))
    student = cursor.fetchone()
    conn.close()

    if student:
        print(f"\n✅ Welcome {student[1]}!")
        while True:
            print("\n--- Student Menu ---")
            print("1. View Profile")
            print("2. View Marks")
            print("3. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                print(f"Roll No: {student[0]}, Name: {student[1]}")
            elif choice == "2":
                view_marks_student(roll_no)
            elif choice == "3":
                break
            else:
                print("⚠️ Invalid choice!")
    else:
        print("⚠️ Invalid Roll No or Password!")

def view_marks_student(roll_no):
    conn = sqlite3.connect("system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, marks FROM grades WHERE roll_no=?", (roll_no,))
    rows = cursor.fetchall()
    if not rows:
        print("⚠️ No marks found!")
    else:
        print(f"\n--- Your Marks ---")
        for row in rows:
            print(f"Subject: {row[0]}, Marks: {row[1]}")
    conn.close()

# ----------------- Teacher Login -----------------
def teacher_login():
    password = input("Enter Teacher Password: ")
    if password != "admin123":
        print("⚠️ Wrong password!")
        return

    while True:
        print("\n--- Teacher Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Marks")
        print("6. Update Marks")
        print("7. View Marks")
        print("8. Logout")

        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            add_marks()
        elif choice == "6":
            update_marks()
        elif choice == "7":
            view_marks()
        elif choice == "8":
            break
        else:
            print("⚠️ Invalid choice!")

# ----------------- Main Program -----------------
def main():
    create_db()
    while True:
        print("\n--- Main Menu ---")
        print("1. Teacher Login")
        print("2. Student Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            teacher_login()
        elif choice == "2":
            student_login()
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice!")

if __name__ == "__main__":
    main()
# else:
#     print("something wrong. Try again..")
