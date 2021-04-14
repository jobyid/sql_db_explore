import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import pymysql

def get_conn(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Exception as ex:
        print(ex)
        return ex

def create_table(db, sentence):
    if sentence.split()[0].lower() == "create":
        try:
            conn = get_conn(db)
            c = conn.cursor()
            t = c.execute(sentence)
            conn.commit()
            conn.close()
            return t
        except Exception as ex:
            print(ex)
            return ex
    raise Exception("Hey come on man, this is the create table function")

def insert_row(sentence, db):
    if sentence.split()[0].lower() == "insert":
        try:
            conn = get_conn(db)
            c = conn.cursor()
            t = c.execute(sentence)
            conn.commit()
            conn.close()
            return t.description
        except Exception as ex:
            print(ex)
            return ex
    raise Exception("What the F*** are you doing this is the insert function")

def select_sql(sentence, db):
    if sentence.split()[0].lower() == "select":
        try:
            conn = get_conn(db)
            c = conn.cursor()
            s = c.execute(sentence)
            conn.commit()

            print(s)
            return s.fetchone()
        except Exception as ex:
            print(ex)
            return ex
    raise Exception("Don't be a dick this is for the Select queries")

def sql_delete(sentence, db):
    if sentence.split()[0].lower() == "delete":
        try:
            conn = get_conn(db)
            c = conn.cursor()
            d = c.execute(sentence)
            conn.commit()
            print(d)
            conn.close()
            return
        except Exception as ex:
            print(ex)
            return ex
    raise Exception("This is for Deleting nothing else")

def drop_table_sql(se, db):
    if se.split()[0].lower() == "drop":
        try:
            conn = get_conn(db)
            c = conn.cursor()
            c.execute(se)
            conn.commit()
            return "Dropped it"
        except Exception as ex:
            print(ex)
            return ex
    raise Exception("No No No, only for dropping tables")

def add_df_to_db(df,name, exists, db, head=0):
    try:
        f = df.to_sql(name, get_conn(db), if_exists=exists,index=0)
        return f
    except Exception as ex:
        print(ex)
        return ex

def upload_csv(name, file, exists, db, head = 0):
    try:
        df = pd.read_csv(file, header=head, index_col=0)
        print(df.head())
        f = df.to_sql(name,get_conn(db), if_exists=exists)
        return f
    except Exception as ex:
        print(ex)
        return ex

def pandas_select_query(s,db, ok=False):
    # Returns a df for the select query
   if s.split(" ")[0].lower() == "SELECT" or ok:
        try:
            df = pd.read_sql_query(s, get_conn(db))
            return df
        except Exception as ex:
            print(ex)
            return ex
   raise Exception("Yo Dude this is for SELECT queries none of this other crap")
