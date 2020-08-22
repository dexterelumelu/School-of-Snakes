from connect import my_cursor
from connect import my_cursor_buffered
from class_list import StudentInfo
from class_list import LogInDetails

def change_username(username):
    session = LogInDetails(username)
    username = session.change_username()
    return username

def change_password(username):
    session = LogInDetails(username)
    session.change_password()

