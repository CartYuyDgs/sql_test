

PORT = 8000
DB_USERNAME = 'root'
DB_PASSWORD = '199411'

DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'sql_test'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)