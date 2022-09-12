import urllib

import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pyodbc

def get_data_ud(id, num, cursor):

    num = str(num[1:])


    cursor.execute(f"""SELECT * FROM user_demographics WHERE user_demographics.Phone_Number_1 = {num}""")

    row = cursor.fetchone()

    print(row)
    if not row:
        cursor.execute(f"""SELECT * FROM user_demographics WHERE user_demographics.Phone_Number_2 = {num}""")
        row = cursor.fetchone()
        print(row)
        if not row:

            cursor.execute(f"SELECT * FROM baseline_answers WHERE user_id = {id}")
            ans = cursor.fetchall()
            for row in ans:
                print(row)
            cursor.execute(f"DELETE FROM baseline_answers WHERE user_id = {id}")
            cursor.execute(f"DELETE FROM monthly_answers WHERE user_id = {id}")
            cursor.execute(f"DELETE FROM users WHERE id = {id}")
            cursor.commit()
            cursor.execute(f"SELECT * FROM baseline_answers WHERE user_id = {id}")
            ans = cursor.fetchall()
            for row in ans:
                print(row)
            # print(f"User: {id} with number {num} not in demos")

if __name__ == "__main__":
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('NAME')
    password = os.environ.get('PASSWORD')


    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users where id>400")

    rows = cursor.fetchall()

    # row = cursor.fetchone()
    # print(row[1])
    # get_data_ud(row[0], row[1], cursor)
    count = 1

    for row in rows:
        print(count)
        print(f"User_id: {row[0]}")
        get_data_ud(row[0], row[1], cursor)
        count +=1

