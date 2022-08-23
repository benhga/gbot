import os
import urllib

import pyodbc
import pandas as pd




if __name__ == "__main__":
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('NAME')
    password = os.environ.get('PASSWORD')


    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()

    # params = urllib.parse.quote_plus(
    #     "DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + server + ';DATABASE=' + database +
    #     ";UID=" + username + ';PWD=' + password)

    # SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params


    # cursor.execute("""Select * into monthly_answers_2 from monthly_answers where 1=2""")
    # cursor.execute(f"""SELECT * FROM user_demographics WHERE user_demographics.Phone_Number_1 = {num}""")
    users = pd.read_sql("SELECT * FROM users", conn)

    answers = pd.read_sql("SELECT * FROM baseline_answers", conn)


    # print(users.describe())
    # print("*"*20)
    #
    #
    # users.drop_duplicates(subset='number', keep='last', inplace=True)
    # print(users.describe())

    # print("*"*20)
    # print(answers.describe())
    cursor.execute(f"""SELECT * FROM baseline_answers""")
    row = cursor.fetchone()

    for row in cursor.fetchall():
        cursor.execute(f"""
        INSERT INTO baseline_answers_2
        (
        [content], [question_id], [user_id]
        )
        VALUES
        (
        {row[1]}, {row[2]}, {row[3]}
        )
        """)


    print("*"*20)

    answers.drop_duplicates(subset=['user_id', 'content', 'question_id'], keep='last', inplace=True)
    # answers.to_sql("baseline_answers", conn, if_exists='replace')


