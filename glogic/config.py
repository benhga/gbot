import os
import urllib.parse
import pyodbc
# noinspection PyUnresolvedReferences
from decouple import config

server = config('SERVER')
database = config('DATABASE')
username = 'myadmin@gbot'
password = config('PASSWORD')

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ';DATABASE=' + database +
                                 ";UID=" + username + ';PWD=' + password)


class MSSQLConfig(object):
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG')
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
