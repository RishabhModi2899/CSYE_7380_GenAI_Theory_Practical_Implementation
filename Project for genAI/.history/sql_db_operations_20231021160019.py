import pymysql

class sql_db_operations:
    df_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password':  
    }

    def __init__(self, conn_string) -> str:
        
