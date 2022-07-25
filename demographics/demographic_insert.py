import os
import urllib.parse
import pandas as pd
import pyodbc

data = pd.read_csv("/Users/benjaminhack/Desktop/GenesisAnalytics/Bot/WageWise/demographics/ww_test_csv.csv")
df = pd.DataFrame(data)

print(df)

server = os.environ.get('SERVER')
database = os.environ.get('DATABASE')
username = os.environ.get('NAME')
password = os.environ.get('PASSWORD')


conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};'
                      'Server={server};'
                      'Database={database};'
                      'UID={username};'
                      'PWD={password};'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute("""IF OBJECT_ID('[dbo].[user_demographics]', 'U') IS NOT NULL
DROP TABLE [dbo].[user_demographics]
GO
-- Create the table in the specified schema
CREATE TABLE [dbo].[user_demographics]
(
    [id] INT NOT NULL PRIMARY KEY, -- Primary Key column
    [programme_name] NVARCHAR(50) NOT NULL,
    [channel] NVARCHAR(50) NOT NULL,
    [date] NVARCHAR(50) NOT NULL,
    [town_or_city] NVARCHAR(50) NOT NULL,
    [province] NVARCHAR(50) NOT NULL,
    [first_name] NVARCHAR(50) NOT NULL,
    [surname] NVARCHAR(50) NOT NULL,
    [id_number] NVARCHAR(50) NOT NULL,
    [phone_number1] NVARCHAR(50) NOT NULL,
    [phone_number2] NVARCHAR(50),
    [home_town] NVARCHAR(50) NOT NULL,
    [sex] NVARCHAR(50) NOT NULL,
    [female] NVARCHAR(50) NOT NULL,
    [age] NVARCHAR(50) NOT NULL,
    [south_african_citizen] NVARCHAR(50) NOT NULL,
    [south_african_citizen_bool] NVARCHAR(50) NOT NULL,
    [population_group] NVARCHAR(50) NOT NULL,
    [population_group_num] NVARCHAR(50) NOT NULL,
    [black_sa_citizen] NVARCHAR(50) NOT NULL,
    [disability] NVARCHAR(50) NOT NULL,
    [disabilty_bool] NVARCHAR(50) NOT NULL,
    [occupation] NVARCHAR(50) NOT NULL,
    [monthly_income] NVARCHAR(50) NOT NULL,
    [income_below_25000pm] NVARCHAR(50) NOT NULL,
    [education] NVARCHAR(50) NOT NULL,
    [attended_workshop] NVARCHAR(50) NOT NULL,

);
GO""")