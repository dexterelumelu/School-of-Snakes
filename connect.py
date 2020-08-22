import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "school"
)

my_cursor = my_db.cursor()
my_cursor_buffered = my_db.cursor(buffered=True)

