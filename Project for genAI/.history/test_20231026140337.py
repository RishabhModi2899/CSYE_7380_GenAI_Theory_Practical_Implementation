def format_sql(sql_query):
    print(sql_)
    lines = sql_query.strip().split('\n')
    print(lines)
    
    sql_lines = [line for line in lines if line.strip().upper().startswith("SELECT") or line.strip().endswith(";")]
    
    return ' '.join(sql_lines).strip()


input = """
This is your SQL:

SELECT COUNT(*) AS total_orders
FROM orders_december
WHERE PRODUCT_TYPES = 'cookies';

This SQL command will count the number of orders for cookies in the "orders_december" table. It will return the total number of orders as "total_orders".
"""
    
print(format_sql(input))