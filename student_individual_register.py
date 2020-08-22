from class_list import StudentInfo
from connect import my_db
from connect import my_cursor


new_student = StudentInfo()
new_student.register()


sql = "INSERT INTO students (firstname, lastname, email, age, username, password) VALUES (%s, %s, %s, %s, %s, %s)"
val = (new_student.firstname, new_student.lastname, new_student.email, new_student.age, new_student.username, new_student.password)

my_cursor.execute(sql, val)
my_db.commit()

print("Your password is Passw0rd\n Log in and change it to be safe")

print("What would you like to do? ")
print("1. Log In\n2. Exit")
response = int(input(":"))

if response == 1:
    from student_log_in import *
else:
    from exit.py import *












