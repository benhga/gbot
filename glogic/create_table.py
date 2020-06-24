import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:gbot.database.windows.net'
database = 'GBotOperational'
username = 'myadmin'
password = 'pipQe8-sadjej-covcaf'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


def initialise_table():
    cursor.execute("DROP TABLE IF EXISTS DummyTable")
    cursor.execute("""
    CREATE TABLE DummyTable (
    id int IDENTITY (1,1) PRIMARY KEY ,
    number varchar(100) NULL,
    user_input varchar(100) NULL,
    date datetime default CURRENT_TIMESTAMP)
                   """)
    cnxn.commit()
    print('ok')




def add_data(num, msg):
    # cursor.execute("INSERT INTO DummyTable VALUES(1,2,3)")
    cursor.execute("insert into DummyTable(number, user_input) values (?,?)",
                   num,
                   msg
                   )
    cnxn.commit()
    print('ok')


# cursor.execute("SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'DummyTable' ")
add_data(5678, "hello")

# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()
#
cursor.close()
cnxn.close()
