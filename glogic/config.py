import urllib.parse
import pyodbc

server = 'tcp:gbot.database.windows.net'
database = 'gbotdata'
username = 'myadmin@gbot'
password = 'pipQe8-sadjej-covcaf'

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ';DATABASE=' + database +
                                 ";UID=" + username + ';PWD=' + password)


class MSSQLConfig(object):
    SECRET_KEY = 'ih8dbs'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_env_files = {
    'ms': 'glogic.config.MSSQLConfig'
}
