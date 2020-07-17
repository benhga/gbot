import os
import urllib.parse
import pyodbc

server = 'tcp:gbot-euro-server.database.windows.net'
database = 'gbot-francedb'
username = 'myadmin@gbot-euro-server'
password = 'pipQe8-sadjej-covcaf'

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ';DATABASE=' + database +
                                 ";UID=" + username + ';PWD=' + password)


class MSSQLConfig(object):
    SECRET_KEY = '018b3f7-vg1(&$^Goib{U(_(*G9-wfeb92-ypv8y06680^&)C0vy-vucrvp689[--#JBC&TQWgiuoccto877050fvh'
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
