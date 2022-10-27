#WeLoveTrees - Ravindra Mangar, Kevin Liu, Mahir Riki
#SoftDev  
#K18 :: (Python+SQLite)3
#Oct 2022
#time spent: error hrs (2 hrs)

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

coursesDict = csv.DictReader(open("courses.csv"))
studentsDict = csv.DictReader(open("students.csv"))

c.execute("CREATE TABLE IF NOT EXISTS courses(code, mark, id)")    # run SQL statement
c.execute("CREATE TABLE IF NOT EXISTS students(name, age, id)")

for row in coursesDict:
  row_dict = dict(row)
  c.execute("INSERT INTO courses VALUES(?, ?, ?)", (row_dict["code"], row_dict["mark"], row_dict["id"]))

for row in studentsDict:
  row_dict = dict(row)
  c.execute("INSERT INTO students VALUES(?, ?, ?)", (row_dict["name"], row_dict["age"], row_dict["id"]))


#VERIFICATION
#c.execute("SELECT * FROM courses")
#print(c.fetchall())
#c.execute("SELECT * FROM students")
#print(c.fetchall())

db.commit() #save changes
db.close()  #close database


