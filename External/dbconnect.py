import mysql.connector

connection = mysql.connector.connect("root","","localhost","dbname")

my_cursor = connection.cursor()

query = "SELECT * FROM student_tbl"
inputs = ("1", "1", 1, "sd")

my_cursor.execute(query, inputs)
my_cursor.executemany(query, inputs)
my_cursor.execute(query)

res= my_cursor.fetchall()
#my_cursor.fetchone() .. my_cursor.fetchmany()

for row in res:
    print(row)

my_cursor.close()
connection.close()