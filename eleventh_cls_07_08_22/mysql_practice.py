# MySQL Database(CRUD Operation) CRUD---> Create Read Update Delete
# Create a Database

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020")
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE family")
    print("Database has been created successfully")
except Exception as e:
    print("The Error is",e)


# CREATE TABLE

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE guardian (Id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Age INT)")
    print("Table has been created successfully")
except Exception as e:
    print("The Error is",e)



# ADD COLUMN

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("ALTER TABLE guardian ADD COLUMN Address VARCHAR(255)")
    print("Adding column successfully")
except Exception as e:
    print("The Error is",e)


# INSERT INTO (VALUE INSERT)
import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO guardian (Name, Age, Address) VALUES ('Alam', 55, 'Satkhira')")
    mydb.commit()
    print("Data insert successfully")
except Exception as e:
    print("The Error is",e)


# INSERT INTO (MANY VALUES)

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    sql = "INSERT INTO guardian (Name, Age, Address) VALUES (%s, %s, %s)"
    val = [
        ("Monira", 40, "Satkhira"),
        ("Zihan", 12, "Satkhira"),
        ("Shohag", 35, "Kalaroa"),
        ("Mizanur", 62, "Kalaroa"),
        ("Rahima", 57, "Kalaroa")
    ]
    cursor.executemany(sql, val)
    mydb.commit()
    print("Value insert successfully")
except Exception as e:
    print("The Error is =",e)


# SHOW TABLES (showing how many tables are here)
import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")

    for i in cursor:
        print(i)
except Exception as e:
    print("The Error is=",e)


# SELECT * FROM

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM guardian")
    res = cursor.fetchall()

    for i in res:
        print(i)
except Exception as e:
    print("The Error is =",e)


# WHERE

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM guardian WHERE Address = 'Kalaroa' ")
    res = cursor.fetchall()

    for i in res:
        print(i)
except Exception as e:
    print("The Error is =", e)


# ORDER BY

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM guardian ORDER BY Age DESC")
    res = cursor.fetchall()

    for i in res:
        print(i)
except Exception as e:
    print("The Error is =", e)


# UPDATE SET WHERE

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("UPDATE guardian SET Age = 42 WHERE Age = 40")
    mydb.commit()
    print("Successfully age updated")
except Exception as e:
    print("The Error is =", e)


# DELETE FROM

import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="2020", database="family")
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM guardian WHERE Age = 12")
    mydb.commit()
    print("Successfully deleted")
except Exception as e:
    print("The Error is =", e)