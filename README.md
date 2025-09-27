🎓 Student Grading System
            

A Python-based Student Grading System that allows teachers and students to manage grades efficiently. Teachers can add, view, update, and delete student records and marks, while students can login securely to check their grades.

🌟 Features
👩‍🏫 Teacher

Add, update, view, and delete student records.

Add, update, and view student marks.

Secure login with password (admin123).

🧑‍🎓 Student

Login with Roll No and Password.

View personal profile.

Check marks for all subjects.

🛠️ Tech & Database

Python 3.x

SQLite3 database

Terminal-based CLI (easy to use)

💻 Installation

Make sure Python 3.x is installed.

Clone this repository:

git clone https://github.com/yourusername/python-projects.git


Navigate to the project folder:

cd python-projects


Run the program:

python Student_Grading_System.py

🚀 Usage

Run the script.

Select Teacher Login or Student Login.

Teacher: enter password admin123 → manage students and grades.

Student: enter Roll No and Password → view profile and marks.

🗄️ Database Structure

Students Table

Column	Type	Description
roll_no	INTEGER	Primary Key
name	TEXT	Student Name
password	TEXT	Student Password

Grades Table

Column	Type	Description
id	INTEGER	Primary Key
roll_no	INTEGER	Foreign Key → Students
subject	TEXT	Subject Name
marks	INTEGER	Marks Obtained
📌 Author

Muhammed Rasmin
