import os
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

class TestConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'test.sqlite'))
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True


config_env_files = {
    'ms': 'glogic.config.MSSQLConfig',
    'test': 'glogic.config.TestConfig'
}
