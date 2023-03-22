# https://flask.palletsprojects.com/en/2.2.x/config/
from os import getenv

DEBUG = True
SECRET_KEY = getenv('SECRET_KEY', 'Hello world')
TESTING = False
# PREFERRED_URL_SCHEME = 'http'
# JSON_AS_ASCII = True
# JSON_SORT_KEYS = True
# JSONIFY_MIMETYPE = 'application/json'

SQLALCHEMY_DATABASE_URI = getenv('DB_CONNECTION_URL', '{0}://{1}:{2}@{3}:{4}/{5}'.format(
    getenv('DB_DIALECT', 'mysql+mysqlconnector'),
    getenv('DB_USERNAME', 'root'),
    getenv('DB_PASSWORD', 'root'),
    getenv('DB_HOST', 'localhost'),
    getenv('DB_PORT', '3306'),
    getenv('DB_NAME', 'app'),
))

SQLALCHEMY_ECHO = False