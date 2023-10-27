def format_sql(self, sql_query):
        lines = sql_query.strip().split('\n')
        
        sql_lines = [line for line in lines if line.strip().upper().startswith("SELECT") or line.strip().endswith(";")]
        
        return ' '.join(sql_lines).strip()
    
# Test the function
input_query = """
   query This is your SQL:

SELECT COUNT(*) AS total_customers
FROM customers; """

print(format_sql())