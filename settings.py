# https://flask.palletsprojects.com/en/2.2.x/config/

DEBUG = True
SECRET_KEY = 'Hello world'
TESTING = False
# PREFERRED_URL_SCHEME = 'http'
# JSON_AS_ASCII = True
# JSON_SORT_KEYS = True
# JSONIFY_MIMETYPE = 'application/json'

# dialect://username:password@host:port/database
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/app'
SQLALCHEMY_ECHO = False