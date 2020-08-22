#!/usr/bin/env python
import os
print("Welcome, what would you like to do? ")
print("1. Sign Up\n2. LogIn")
response = int(input(":"))

if response == 1:
    from student_individual_register import *
else:
    from student_log_in import *