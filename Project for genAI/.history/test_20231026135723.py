def format_sql(self, sql_query):
    lines = sql_query.strip().split('\n')
    
    sql_lines = [line for line in lines if line.strip().upper().startswith("SELECT") or line.strip().endswith(";")]
    
    return ' '.join(sql_lines).strip()
    
forma