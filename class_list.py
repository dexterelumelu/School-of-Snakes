class StudentInfo:
    def register(self):
        self.firstname = input("What is your first name? ")
        self.lastname = input("What is your lastname? ")
        self.age = int(input("What is your age? "))
        self.password = "Passw0rd!"
        self.email = StudentInfo.verify_email(self)
        self.username = StudentInfo.verify_username(self)

    def verify_email(self):
        email = input("What is the email address? ")
        sql = "SELECT * FROM students WHERE email ='" + email + "'"
        my_cursor_buffered.execute(sql)

        while my_cursor_buffered.rowcount > 0:
            print("Email Taken")
            email = input("Choose New Email: ")
            sql = "SELECT * FROM students WHERE email ='" + email + "'"
            my_cursor_buffered.execute(sql)

        return email

    def verify_username(self):
        username = input("New username? ")
        sql = "SELECT * FROM students WHERE username ='" + username + "'"
        my_cursor_buffered.execute(sql)

        while my_cursor_buffered.rowcount > 0 and username != "root":
            print("Username Taken")
            username = input("Choose New Username: ")
            sql = "SELECT * FROM students WHERE username ='" + username + "'"
            my_cursor_buffered.execute(sql)

        return username

    def show_info(self, username):
        my_cursor.execute("SELECT * FROM students WHERE username = '" + username + "'")
        result = my_cursor.fetchone()
        print("Firstname = " + result[1])
        print("Lastname = " + result[2])
        print("Email = " + result[3])
        print("Age = " + str(result[4]))
        print("Username = " + result[5])


class LogInDetails():
    def __init__(self, username):
        self.username = username

    def change_username(self):
        check_username = StudentInfo.verify_username(self)
        my_cursor.execute("UPDATE students SET username = '" + check_username + "' WHERE username = '" + self.username + "'")
        my_db.commit()

    def change_password(self):
        my_cursor.execute("SELECT password FROM students WHERE username = '" + self.username + "'")
        result = my_cursor.fetchone()
        old_password_confirmed = result[0]
        old_password_input = input("What was your old password? ")

        while True:
            if old_password_input != old_password_confirmed:
                print("Incorrect Input")
                old_password_input = input("What was your old password? ")
            else:
                break

        new_password = input("What is your new password? ")
        while True:
            if new_password == old_password_input:
                print("Password cannot be old password")
                new_password = input("What is your new password? ")
            else:
                my_cursor.execute("UPDATE students SET password ='" + new_password + "' WHERE password = '" + old_password_confirmed + "'")
                my_db.commit()
                print("Password Updated!")
                break

class SuperUser:
    def add_student(self):
        StudentInfo.register(self)
    def view_student(self, username):
        StudentInfo.show_info(self, username)
    def view_all_students(self, key):
        if key == '*':
            my_cursor.execute("SELECT * FROM students")
        else:
            my_cursor.execute("SELECT * FROM students ORDER BY " + key)

        result = my_cursor.fetchall()

        for x in result:
            print(x)
    def delete_student(self, username):
        my_cursor_buffered.execute("DELETE FROM students WHERE username = '" + username + "'")


from connect import  my_db
from connect import my_cursor_buffered
from connect import my_cursor



