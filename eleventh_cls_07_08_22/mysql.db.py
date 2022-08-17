
# import mysql.connector

# CREATE DATABASE
# my_database = mysql.connector.connect(host="localhost", user="root", password="2020")
# my_cursor = my_database.cursor()
#   #my_cursor.execute("CREATE DATABASE college")
# my_cursor.execute("SHOW DATABASES")

# for i in my_cursor:
#     print(i)


# CREATE TABLE

# my_database = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# my_cursor = my_database.cursor()
# my_cursor.execute("CREATE TABLE student_info (name VARCHAR(150), age INTEGER(10))")


# INSERT INTO (insert values)

# my_database = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# my_cursor = my_database.cursor()
# val = my_cursor.execute("INSERT INTO student_info (name, age) values('Zishan', 22)")
# my_database.commit()
#
# print("Value Inserted")

# my_database = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# my_cursor = my_database.cursor()
# val = my_cursor.execute("INSERT INTO student_info (name, age) VALUES('Razib', 23)")
# my_database.commit()
#
# print(my_cursor.rowcount,"row has been created")


# executemany
# my_database = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# my_cursor = my_database.cursor()
# sql = "INSERT INTO student_info (name, age) VALUES(%s, %s)"
# val = [
#     ("Abir", 24),
#     ("Faruk", 23),
#     ("Synthea", 21),
#     ("Disha", 25)
# ]
# my_cursor.executemany(sql, val)
# my_database.commit()
# print(my_cursor.rowcount,"new row is inserted")

# SELECT

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM student_info")
# res = mycursor.fetchall()
# for i in res:
#     print(i)

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# mycursor = mydb.cursor()
# mycursor.execute("SELECT name FROM student_info")
# res = mycursor.fetchall()
# for i in res:
#     print(i)

# WHERE

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM student_info WHERE age = 23")
# res = mycursor.fetchall()
#
# for i in res:
#     print(i)

# ORDER BY

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# cursor = mydb.cursor()
# cursor.execute("SELECT * FROM student_info ORDER BY name DESC")
# res = cursor.fetchall()
# for i in res:
#     print(i)

# DELETE FROM

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
# mycursor = mydb.cursor()
# mycursor.execute("DELETE FROM student_info WHERE age = 23")
# mydb.commit()


# UPDATE

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="college")
mycursor = mydb.cursor()
mycursor.execute("UPDATE student_info SET name = 'Naim' WHERE name = 'Abir' ")
mydb.commit()
