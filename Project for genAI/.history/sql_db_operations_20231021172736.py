import pymysql

class sql_db_operations:
    df_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'admin',
        'db': 'csye7380_genai'
    }

    def __init__(self) -> None:
        pass

    def connect(self, conn_string):
        try:
            connection = pymysql.connect(**self.df_config)
            print('CONNECTION TO DB ESTABLISHED!')
        except Exception as e:
            print(f'An exception has occurred')

    def close_connection(self, co):