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
            'db': os.environ.get('db'), 
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
        print(categories_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Categories (
                        ID INT PRIMARY KEY,
                        PRODUCT_TYPE VARCHAR(255) NOT NULL
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in categories_excel_data.iterrows():
                    print(f"row = {row}")
                    insert_query_sql = 'INSERT INTO categories (ID, PRODUCT_TYPE) VALUES (%s, %s)'
                    cursor.execute(insert_query_sql,
                                   (int(row['ID']), str(row['Product Types'])))
            self.connection.commit()
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
# sql_conn.create_populate_Categories() creat
sql_conn.close_connection()
