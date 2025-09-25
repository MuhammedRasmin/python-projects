import sqlite3
def creat():
    conn=sqlite3.connect("power.db")
    crsr=conn.cursor()
    crsr.execute("""CREATE TABLE IF NOT EXISTS uchiha(
                 roll TEXT PRIMARY KEY,
                 name TEXT,
                 email TEXT,
                 password TEXT)""")
    conn.commit()
    conn.close()


def teacher_menu():
    while True:
        print("\n=== STUDENT DATABASE MENU ===")
        print("1.ADD STUDENT")
        print("2.View students")
        print("3.update students")
        print("4.Delete students")
        print("5.Exit")

        choice=input("Enter your choice(1-5): ")

        conn=sqlite3.connect("power.db")
        crsr=conn.cursor()

        if choice=="1":
            roll=input("Enter roll no: ")
            name=input("Enter name: ")
            email=input("Enter email: ")
            password=input("Enter passwod: ")
            try:
                crsr.execute("""INSERT INTO uchiha VALUES(?,?,?,?)""", (roll,name,email,password))
                conn.commit()
                print("✅ sharingan added successfully!")
            except sqlite3.IntegrityError:
                print("❌ Roll number already exists!")

        elif choice=="2":
            crsr.execute("SELECT * FROM uchiha")
            rows=crsr.fetchall()
            if rows:
                print("\n--- Uchiha List ---")
                for r in rows:
                    print(f"Rows: {r[0]}, Name: {r[1]}, Email: {r[2]}")
            else:
                print("No uchihas found")  

        elif choice=="3":
            roll=input("Enter roll no to update: ") 
            crsr.execute("""SELECT * FROM uchiha WHERE roll=?""",(roll,)) 
            if crsr.fetchone():
                name=input("Enter new name: ")
                email=input("Enter new emaail: ")
                password=input("Enter new password: ")
                crsr.execute(""""UPDATE uchiha SET name=?,email=?,password=? WHERE roll=?""",
                             (name,email,password,roll))
                conn.commit()
                print("✅ Student updated successfully!")
            else:
                print("❌ Student not found.")

        elif choice=="4":
            roll=input("Enter roll to dalete: ")
            crsr.execute("""DELETE FROM uchiha WHERE roll=?""",(roll))
            conn.commit()
            if crsr.rowcount > 0:
                print("Deleted successfully")
            else:
                print("student not found")

        elif choice=="5":
            print("Teacher menu....")
            conn.close()
            break

        else:
            print("Invalid choice")

        conn.close()   



def student_menu(username,password):
    conn=sqlite3.connect("power.db")
    crsr=conn.cursor()
    crsr.execute("""SELECT * FROM uchiha WHERE name=? AND password=?""",(username,password))
    row=crsr.fetchone()
    if row:
        print(f"\nWelcom {row[1]}!")
        print(f"Roll: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    else:
        print("No details found. Check username or password")
    conn.close()


def login():
    print("====== Login ======")
    user_type=input("Login as (teacher/student): ")
    if user_type.lower()=="teacher":
        username=input("Enter teacher username: ")
        password=input("Enter teacher password: ")

        if username=="teacher" and password=="1234":
            print("✅ Teacher login successful!")
            teacher_menu()
        else:
            print("❌ Invalid teacher credentials!")

    elif user_type.lower()=="student":
        username=input("Enter student username: ")
        password=input("Enter student password: ")
        student_menu(username,password)

    else:
        print("❌ Invalid choice!")


creat()
login()        





