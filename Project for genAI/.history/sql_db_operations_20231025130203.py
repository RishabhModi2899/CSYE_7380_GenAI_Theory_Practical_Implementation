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
            
    def get_db_connection(self):
        return self.conn
            
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
            
    def create_populate_Customers(self):
        customers_excel_data = pd.read_excel("C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Customers.xlsx")
        print(customers_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Customers (
                        ID INT PRIMARY KEY,
                        FIRST_NAME VARCHAR(255) NOT NULL,
                        LAST_NAME VARCHAR(255) NOT NULL,
                        STREET_ADDRESS VARCHAR(255) NOT NULL,
                        CITY VARCHAR(255) NOT NULL,
                        STATE VARCHAR(255) NOT NULL,
                        ZIPCODE VARCHAR(255) NOT NULL,
                        EMAIL VARCHAR(255),
                        ADD_TO_MAILING_LIST VARCHAR(255) NOT NULL,
                        PHONE_NUMBER VARCHAR(255) NOT NULL,
                        OTHER_NOTES VARCHAR(255)
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in customers_excel_data.iterrows():
                    print(f"row = {row}")
                    insert_query_sql = 'INSERT INTO Customers (ID, FIRST_NAME, LAST_NAME, STREET_ADDRESS, CITY, STATE, ZIPCODE, EMAIL, ADD_TO_MAILING_LIST, PHONE_NUMBER, OTHER_NOTES) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(insert_query_sql,
                                   (int(row['ID']), str(row['First Name']), str(row['Last Name']), str(row['Street Address']), str(row['City']), row['State'], str(row['Zip Code']), str(row['Email']), str(row['Add to Mailing List?']), str(row['Phone Number']), str(row['Other Notes'])))
            self.connection.commit()
        except Exception as e:
            print(f'An exception has occurred: {e}')
            
    def create_populate_MenuItems(self):
        menuItems_excel_data = pd.read_excel("C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Menu Items.xlsx")
        print(menuItems_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Menu_Items (
                        ID INT PRIMARY KEY,
                        PRODUCT_ID INT NOT NULL,
                        SALES_UNIT_ID INT NOT NULL,
                        PRICE VARCHAR(255) NOT NULL
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in menuItems_excel_data.iterrows():
                    print(f"row = {row}")
                    insert_query_sql = 'INSERT INTO Menu_Items (ID, PRODUCT_ID, SALES_UNIT_ID, PRICE) VALUES (%s, %s, %s, %s)'
                    cursor.execute(insert_query_sql,
                                   (int(row['ID']), int(row['Product ID']), int(row['Sales Unit ID']), str(row['Price'])))
            self.connection.commit()
        except Exception as e:
            print(f'An exception has occurred: {e}')
            
    def create_populate_OrderItems(self):
        orderItems_excel_data = pd.read_excel("C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Order Items.xlsx")
        print(orderItems_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Order_Items (
                        ID INT PRIMARY KEY,
                        ORDER_ID INT NOT NULL,
                        MENU_ITEM_ID INT NOT NULL,
                        QUANTITY INT NOT NULL
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in orderItems_excel_data.iterrows():
                    print(f"row = {row}")
                    insert_query_sql = 'INSERT INTO Order_Items (ID, ORDER_ID, MENU_ITEM_ID, QUANTITY) VALUES (%s, %s, %s, %s)'
                    cursor.execute(insert_query_sql,
                                   (int(row['ID']), int(row['Order ID']), int(row['Menu Item ID']), int(row['Quantity'])))
            self.connection.commit()
        except Exception as e:
            print(f'An exception has occurred: {e}')
            
    def create_populate_OrdersTable(self):
        ordersTable_excel_data = pd.read_excel("C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Orders Table.xlsx")
        print(ordersTable_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Orders_Table (
                        ID INT PRIMARY KEY,
                        CUSTOMER_ID INT NOT NULL,
                        PAID VARCHAR(255) NOT NULL,
                        PRE_ORDER VARCHAR(255) NOT NULL,
                        NOTES VARCHAR(255),
                        PICKUP_DATE VARCHAR(255)
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in ordersTable_excel_data.iterrows():
                    print(f"row = {row}")
                    insert_query_sql = 'INSERT INTO Orders_Table (ID, CUSTOMER_ID, PAID, PRE_ORDER, NOTES, PICKUP_DATE) VALUES (%s, %s, %s, %s, %s, %s)'
                    cursor.execute(insert_query_sql,
                                   (int(row['ID']), int(row['Customer ID']), str(row['Paid']), str(row['Pre Order']), str(row['Notes']), str(row['Pickup Date'])))
            self.connection.commit()
        except Exception as e:
            print(f'An exception has occurred: {e}')
            
    def create_populate_OrdersDecember(self):
        ordersDecember_excel_data = pd.read_excel("C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Orders_ December.xlsx")
        print(ordersDecember_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Orders_December (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        PRODUCT_TYPES VARCHAR(255),
                        PRODUCT_NAME VARCHAR(255) NOT NULL,
                        SALES_UNIT VARCHAR(255) NOT NULL,
                        VALUE_OF_SALES_UNIT INT NOT NULL,
                        NUMBER_OF_SALES_UNIT_SOLD INT NOT NULL,
                        ACTUAL_NUMBER_SOLD INT
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in ordersDecember_excel_data.iterrows():
                    print(f"row = {row}")
                    if index == len(ordersDecember_excel_data) - 1:
                        continue
                    insert_query_sql = 'INSERT INTO Orders_December (PRODUCT_TYPES, PRODUCT_NAME, SALES_UNIT, VALUE_OF_SALES_UNIT, NUMBER_OF_SALES_UNIT_SOLD, ACTUAL_NUMBER_SOLD) VALUES (%s, %s, %s, %s, %s, %s)'
                    cursor.execute(insert_query_sql,
                                   (str(row['Product Types']), str(row['Product Name']), str(row['Sales Unit']), int(row['Value of Sales Unit']), int(row['# of Sales Unit Sold']), int(row['Actual # Sold'])))
            self.connection.commit()
        except Exception as e:
            print(f'An exception has occurred: {e}')
            
    def create_populate_ProductsTable(self):
        productsTable_excel_data = pd.read_excel("C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Products Table.xlsx")
        print(productsTable_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Products_Table (
                        ID INT PRIMARY KEY,
                        PRODUCT_NAME VARCHAR(255) NOT NULL,
                        DESCRIPTION VARCHAR(255)
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in productsTable_excel_data.iterrows():
                    print(f"row = {row}")

                    insert_query_sql = 'INSERT INTO Products_Table (ID, PRODUCT_NAME, DESCRIPTION) VALUES (%s, %s, %s)'
                    cursor.execute(insert_query_sql,
                                   (str(row['ID']), str(row['Product Name']), str(row['Description'])))
            self.connection.commit()
        except Exception as e:
            print(f'An exception has occurred: {e}')
            
    def create_populate_SalesUnit(self):
        salesUnit_excel_data = pd.read_excel("C:/Users/risha/OneDrive/Documents/CSYE7380/CSYE_7380_GenAI_Theory_Practical_Implementation/Project for genAI/Sales Unit.xlsx")
        print(salesUnit_excel_data)
              
        try:
            with self.connection.cursor() as cursor:
                create_table_sql = """
                    CREATE TABLE IF NOT EXISTS Sales_Unit (
                        ID INT PRIMARY KEY,
                        PRODUCT_NAME VARCHAR(255) NOT NULL,
                        SALES_UNIT_VAL VARCHAR(255)
                    )
                """
                cursor.execute(create_table_sql)
                
                for index, row in salesUnit_excel_data.iterrows():
                    print(f"row = {row}")

                    insert_query_sql = 'INSERT INTO Sales_Unit (ID, PRODUCT_NAME, SALES_UNIT_VAL) VALUES (%s, %s, %s)'
                    cursor.execute(insert_query_sql,
                                   (str(row['ID']), str(row['Product Name']), str(row['SalesUnit Val'])))
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
# sql_conn.create_populate_Categories() # creating and populating the categories table
# sql_conn.create_populate_Customers() # creating and populating the categories table
# sql_conn.create_populate_MenuItems() # creating and populating the Menu_Items table
# sql_conn.create_populate_OrderItems() # creating and populating the Order_Items table
# sql_conn.create_populate_OrdersTable() # creating and populating the Orders_Table table
# sql_conn.create_populate_OrdersDecember() # creating and populating the Orders_December table
# sql_conn.create_populate_ProductsTable() # creating and populating the Products table table
sql_conn.create_populate_SalesUnit() # creating and populating the Products table table
sql_conn.close_connection()
