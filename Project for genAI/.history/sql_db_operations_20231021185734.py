import pymysql as psql
from dotenv import load_dotenv
import os
import pandas as pd

class sql_db_operations:
    connection = None
    df_config = None

    def __init__(self) -> None:
        load_dotenv()

        self.df_config = {
            'host': 'localhost',
            'port': int(os.environ.get('port')),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'db': os.environ.get('csye7380_genai'), 
            'charset': 'utf8mb4',
            'cursorclass': psql.cursors.DictCursor
        }

    def connect(self):
        try:
            self.connection = psql.connect(**self.df_config)
            print('CONNECTION TO DB ESTABLISHED!')
        except Exception as e:
            print(f'An exception has occurred: {e}')
            
    def create_populate_Categories(self):
        categories_excel_data = pd.read_excel('C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Categories.xlsx')
        try:
            with self.connection.cursor() as cursor:
                for index, row in categories_excel_data.iterrows():
                    sql = 'INSERT INTO Categories ID, Product Types VALUES %s, %s'
                    cursor.execute(sql, (row['ID'], row['Product Types']))
                cursor.co
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
sql_conn.create_populate_Categories()
sql_conn.close_connection()
