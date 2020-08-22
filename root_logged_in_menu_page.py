from class_list import SuperUser
response = int(input("What would you like to do?\n"
                 "1. ADD A STUDENT\n"
                 "2. VIEW A STUDENT\n"
                 "3. VIEW ALL STUDENTS\n"
                 "4. DELETE A STUDENT\n"
                 ":     "))



if response == 1:
    logged_in_super_user = SuperUser()
    logged_in_super_user.add_student()
if response == 2:
    username = input("What is the name of the student you want to view? ")
    logged_in_super_user = SuperUser()
    logged_in_super_user.view_student(username)
if response == 3:
    sub_response = int(input("View by:\n"
          "1. ALL\n"
          "2. ID\n"
          "3. LASTNAME\n"
          "4. Email\n"
          "5. Username\n"
          ":    "))
    logged_in_super_user = SuperUser()
    if sub_response == 1:
        key = "*"
        logged_in_super_user.view_all_students(key)
    elif sub_response == 2:
        key = "ID"
        logged_in_super_user.view_all_students(key)
    elif sub_response == 3:
        key = "lastname"
        logged_in_super_user.view_all_students(key)
    elif sub_response == 4:
        key = "email"
        logged_in_super_user.view_all_students(key)
    elif sub_response == 5:
        key = "username"
        logged_in_super_user.view_all_students(key)
elif response == 4:
    username = input("What is the Username: ")
    logged_in_super_user = SuperUser()
    logged_in_super_user.delete_student(username)
else:
    print("Invalid Input\nLogging Out")
