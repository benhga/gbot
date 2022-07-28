import urllib

import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pyodbc

def get_data(num):
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('NAME')
    password = os.environ.get('PASSWORD')


    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM user_demographics_test100 WHERE user_demographics_test100.Phone_Number_1 = {num}""")

    row = cursor.fetchone()

    print(row)

    if row:
        return True, row[9]
    else:
        cursor.execute(f"""SELECT * FROM user_demographics_test100 WHERE user_demographics_test100.Phone_Number_2 = {num}""")
        row = cursor.fetchone()
        if row:
            return True, row[8]

        return False, 0

if __name__ == "__main__":
    num = "+27832682716"
    print(get_data(num))