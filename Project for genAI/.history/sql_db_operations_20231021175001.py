import pymysql as psql
from dotenv import load_dotenv
import os

class sql_db_operations:
    connection = None

    def __init__(self) -> None:
        load_dotenv()

        df_config = {
            'host': 'localhost',
            'port': os.environ.get('port'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'db': os.environ.get('csye7380_genai')
        }
        print(self.df_config)

    def connect(self):
        try:
            self.connection = psql.connect(**self.df_config)
            print('CONNECTION TO DB ESTABLISHED!')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def close_connection(self):
        try:
            self.connection.close()
            print('Connection to DB has been closed!')
        except Exception as e:
            print(f'Exception has occurred: {e}')


# Driver Code
sql_conn = sql_db_operations()
sql_conn.connect()
sql_conn.close_connection()
