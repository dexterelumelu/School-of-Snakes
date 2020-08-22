from student_log_in import username
from update_info import change_username
from update_info import change_password

print("Welcome " + username + "!")
response = int(input("What would you like to do?\n"
                     "1. Change Username\n"
                     "2. Change Password\n"
                     "3. Exit\n"
                     ":    "))


while True:
    if response == 1:
        username = change_username(username)
        break
    elif response == 2:
        change_password(username)
        break
    elif response == 3:
        break
    else:
        response = int(input("Invalid response\n\n\nWhat would you like to do?\n"
                             "1. Change Username\n"
                             "2. Change Password\n"
                             "3. Exit"))