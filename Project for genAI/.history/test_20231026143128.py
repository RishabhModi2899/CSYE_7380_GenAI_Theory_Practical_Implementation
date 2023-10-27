import re

def extract_sql_queries(s):
    # This regular expression looks for strings that start with words like SELECT, INSERT, etc. 
    # and end with a semicolon.
    pattern = r'\b(SELECT|INSERT|UPDATE|DELETE)\b[^;]*;'
    
    return re.findall(pattern, s, re.IGNORECASE)

# Testing
text = """
This is some text. 
SELECT name FROM users WHERE age > 21;
Here's more text. 
INSERT INTO users(name, age) VALUES ('John', 30);
Even more unrelated text.
"""

queries = extract_sql_queries(text)
for q in queries:
    print(q)
This function will capture basic SQL queries from a given string. However, it has its limitations:

Doesn't handle nested queries or more complex SQL structures well.
Doesn't handle SQL queries split across multiple lines without spaces between lines.
Might falsely identify non-SQL segments if they happen to match the pattern.
For a comprehensive solution, consider using dedicated SQL parsers or libraries, but they might be overkill for simpler tasks. Adjustments to the function and regex pattern may be needed based on the specific SQL structures you expect.








input = """
This is your SQL:

SELECT COUNT(*) AS total_orders
FROM orders_december
WHERE PRODUCT_TYPES = 'cookies';

This SQL command will count the number of orders for cookies in the "orders_december" table. It will return the total number of orders as "total_orders".
"""
    
print(format_sql(input))