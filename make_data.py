import pandas as pd
import numpy as np
import database_funcs as dbf
import re
import sqlite3


new_table   = """CREATE TABLE student (
                                    name varchar(20) NOT NULL,
                                    surname varchar(20) NOT NULL DEFAULT 'a',
                                    id int NOT NULL PRIMARY KEY,
                                    country varchar(20),
                                    FOREIGN KEY(id) REFERANCES projects(st)
                                );"""
new_row     = """INSERT INTO student(name, surname, id, country) VALUES('James','Smith',2,'France')"""
test_select = """SELECT COUNT(*) FROM student"""
all_rows    = """SELECT * FROM student2"""
delete_row  = """DELETE FROM student WHERE id = 0"""
new_table2   = """CREATE TABLE student2 (
                                    name varchar(20) NOT NULL,
                                    surname varchar(20) NOT NULL DEFAULT 'a',
                                    id int NOT NULL PRIMARY KEY,
                                    country varchar(20),
                                    FOREIGN KEY(id) REFERANCES projects(st)
                                );"""

#x = dbf.create_table("databases/strive_demo.db", new_table)
#print(x)



students = pd.read_csv('datasets/students.csv')

#print(students.head())

#d = dbf.sql_delete(delete_row,"databases/strive_demo.db")


#dbf.add_df_to_db(students,"students", exists="replace", db="databases/strive_demo.db")
name_val = []
surnames = []
id = []
country = []
for col_name, data in students.items():
    if col_name == "name":
        for d in data:
            name_val.append(d)
    elif col_name == "surname":
        for d in data:
            surnames.append(d)
    elif col_name == "id":
        for d in data:
            id.append(d)
    elif col_name == "country":
        for d in data:
            country.append(d)

print(name_val)
vs = ""
for i in range(0,len(name_val)):
    x = "INSERT INTO student(name, surname, id, country) VALUES('{}','{}','{}','{}')".format(name_val[i], surnames[i],id[i],country[i])
    #dbf.insert_row(x, "databases/strive_demo.db")


ndf = dbf.upload_csv("student2", 'datasets/students.csv',"replace", "databases/strive_demo.db")
print(ndf)
#big_insert = """INSERT INTO student(name, surname, id, country) VALUES(""" + vs[:-1] + ")"
#dbf.insert_row(big_insert, "databases/strive_demo.db")
q = dbf.select_sql(all_rows, "databases/strive_demo.db")
print(q)
qdf = dbf.pandas_select_query(all_rows, "databases/strive_demo.db")
print(qdf.head())
