def format_sql(sql_query):
    print(sql_query)
    lines = sql_query.strip().split('\n')
    print(lines)
    
    collecting = False
    sql_lines = []
    
    for line in lines:
        stripped_line = line.strip().upper()
        
        if stripped_line.startswith("SELECT"):
            collecting = True
        
        if collecting:
            sql_lines.append(line.strip())
            
            if stripped_line.endswith(";"):
                collecting = False

    return ' '.join(sql_lines).strip()

# Testing
query = """
-- Some comments here
SELECT name, age
FROM users
WHERE age > 21
;

Another text here

INSERT INTO users(name, age) VALUES ('John', 30);
"""

formatted_query = format_sql(query)
print("\nFormatted SQL:\n", formatted_query)
input = """
This is your SQL:

SELECT COUNT(*) AS total_orders
FROM orders_december
WHERE PRODUCT_TYPES = 'cookies';

This SQL command will count the number of orders for cookies in the "orders_december" table. It will return the total number of orders as "total_orders".
"""
    
print(format_sql(input))