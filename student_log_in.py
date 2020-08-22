from connect import my_cursor_buffered
from class_list import StudentInfo


username = input("usename: ")


while True:
    if username == "root":
        my_cursor_buffered.execute("SELECT password FROM students WHERE username = 'root'")
        result = my_cursor_buffered.fetchone()
        password_correct = result[0]

        password_input = input("input root user password")

        while password_correct != password_input:
            password_input = input("Wrong! TRY AGAIN")

        from root_logged_in_menu_page import *
    else:
        my_cursor_buffered.execute("SELECT * FROM students WHERE username = '" + username + "'")

        if my_cursor_buffered.rowcount > 0:
            result = my_cursor_buffered.fetchone()

            firstname = result[1]
            password_correct = result[6]

            print("Welcome " + firstname + "!")
            password_input = input("What is your password: ")

            if password_correct == password_input:
                break
            else:
                while password_input != password_correct:
                    password_input = input("Incorrect! Try again: ")
            break

        else:
            username = input("No such username, try again: ")

from logged_in_menu_page import *






