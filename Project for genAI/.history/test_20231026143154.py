import re

def extract_sql_queries(s):
    # This regular expression looks for strings that start with words like SELECT, INSERT, etc. 
    # and end with a semicolon.
    pattern = r'\b(SELECT|INSERT|UPDATE|DELETE)\b[^;]*;'
    
    return re.findall(pattern, s, re.IGNORECASE)




input = """
This is your SQL:

SELECT COUNT(*) AS total_orders
FROM orders_december
WHERE PRODUCT_TYPES = 'cookies';

This SQL command will count the number of orders for cookies in the "orders_december" table. It will return the total number of orders as "total_orders".
"""
    
print(format_sql(input))