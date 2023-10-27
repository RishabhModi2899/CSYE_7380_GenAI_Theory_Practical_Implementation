def format_sql(self, sql_query):
        lines = sql_query.strip().split('\n')
        
        sql_lines = [line for line in lines if line.strip().upper().startswith("SELECT") or line.strip().endswith(";")]
        
        return ' '.join(sql_lines).strip()
    
format_sql("This is your SQL: \n
SELECT COUNT(*) AS total_customers
FROM customers;)