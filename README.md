Student Grading System

A Python-based Student Grading System that allows teachers and students to manage grades efficiently.
Teachers can add, view, update, and delete student records and marks, while students can securely login to check their grades.






##Features:

Teacher

Add, update, view, and delete student records

Add, update, and view student marks

Secure login with password (admin123)


Student

Login with Roll No and Password

View personal profile

Check marks for all subjects


##Technology

Python 3.x

SQLite3 database

Terminal-based CLI interface


##Installation

Ensure Python 3.x is installed on your system

Clone this repository:

git clone https://github.com/yourusername/python-projects.git


Navigate into the project folder:

cd python-projects


Run the application:

python Student_Grading_System.py


Usage

Run the script

Select Teacher Login or Student Login

Teacher Login:

Password: admin123


Manage students and marks via menu options

Student Login:

Enter Roll No and Password

View profile and marks


Sample CLI
--- Main Menu ---
1. Teacher Login
2. Student Login
3. Exit

--- Teacher Menu ---
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Add Marks
6. Update Marks
7. View Marks
8. Logout

--- Student Menu ---
1. View Profile
2. View Marks
3. Logout

Database Structure
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


Developed by - Muhammed Rasmin
