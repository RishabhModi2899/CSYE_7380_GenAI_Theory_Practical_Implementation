import pymysql

class sql_db_operations:
    df_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'admin',
        'db': 'csye7380_genai'
    }

    def __init__(self, conn_string) -> str:
        try:
            connection = pymysql.connect(**self.df_config)
