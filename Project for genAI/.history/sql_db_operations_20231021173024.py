import pymysql

class sql_db_operations:
    connection = None

    df_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'admin',
        'db': 'csye7380_genai'
    }

    def __init__(self) -> None:
        pass

    def connect(self):
        try:
            self.connection = pymysql.connect(**self.df_config)
            print('CONNECTION TO DB ESTABLISHED!')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def close_connection(self):
        try:
            print('Connection to DB has been closed!')
        except Exception as e:
            print(f'Exception has occurred: {e}')


# Driver Code
