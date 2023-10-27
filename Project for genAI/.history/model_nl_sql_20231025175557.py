import openai
import os
from dotenv import load_dotenv
import panel as pn
from sql_db_operations import sql_db_operations
import pymysql
import pandas as pd

load_dotenv()

openai.api_key=os.environ.get('openai_key')

context = [ {'role':'system', 'content':"""
you are a bot to assist in create SQL commands, all your answers should start with \
this is your SQL, and after that an SQL that can do what the user request. \
Your Database is composed by a SQL database with some tables. \
Try to Maintain the SQL order simple.
Put the SQL command in white letters with a black background, and just after \
a simple and concise text explaining how it works. 
If the user ask for something that can not be solved with an SQL Order \
just answer something nice and simple and ask him for something that \
can be solved with SQL. 
"""} ]

context.append( {'role':'system', 'content':"""
first table: 
{
  "tableName": "categories",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "PRODUCT_TYPE",
      "type": "string"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
second table: 
{
  "tableName": "customers",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "FIRST_NAME",
      "type": "string"
    },
    {
      "name": "LAST_NAME",
      "type": "string"
    },
    {
      "name": "STREET_ADDRESS",
      "type": "string"
    },
    {
      "name": "CITY",
      "type": "string"
    },
    {
      "name": "STATE",
      "type": "string"
    },
    {
      "name": "ZIPCODE",
      "type": "STRING"
    },
    {
      "name": "EMAIL",
      "type": "STRING"
    },
    {
      "name": "ADD_TO_MAILING_LIST",
      "type": "STRING"
    },
    {
      "name": "PHONE_NUMBER",
      "type": "STRING"
    },
    {
      "name": "OTHER_NOTES",
      "type": "STRING"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
third table: 
{
  "tableName": "menu_items",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "PRODUCT_ID",
      "type": "int"
    },
    {
      "name": "SALES_UNIT_ID",
      "type": "int"
    },
    {
      "name": "PRICE",
      "type": "string"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
fourth table: 
{
  "tableName": "order_items",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "ORDER_ID",
      "type": "int"
    },
    {
      "name": "MENU_ITEM_ID",
      "type": "int"
    },
    {
      "name": "QUANTITY",
      "type": "int"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
fifth table: 
{
  "tableName": "orders_december",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "PRODUCT_TYPES",
      "type": "string"
    },
    {
      "name": "PRODUCT_NAME",
      "type": "string"
    },
    {
      "name": "SALES_UNIT",
      "type": "string"
    },
    {
      "name": "VALUE_OF_SALES_UNIT",
      "type": "int"
    },
    {
      "name": "NUMBER_OF_SALES_UNIT_SOLD",
      "type": "int"
    },
    {
        "name": "ACTUAL_NUMBER_SOLD",
        "type": "int"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
sixth table: 
{
  "tableName": "orders_table",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "CUSTOMER_ID",
      "type": "int"
    },
    {
      "name": "PAID",
      "type": "string"
    },
    {
      "name": "PRE_ORDER",
      "type": "string"
    },
    {
      "name": "NOTES",
      "type": "string"
    },
    {
      "name": "PICKUP_DATE",
      "type": "string"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
seventh table: 
{
  "tableName": "products_table",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "PRODUCT_NAME",
      "type": "string"
    },
    {
      "name": "DESCRIPTION",
      "type": "string"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
eight table: 
{
  "tableName": "sales_unit",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "PRODUCT_NAME",
      "type": "string"
    },
    {
      "name": "SALES_UNIT_VAL",
      "type": "string"
    }
  ]
}
"""
})

class SQLApp:
    def __init__(self) -> None:
        # self.sql_db_ops = sql_db_operations()
        self.sql_db_ops = sql_db_operations()
        self.last_sql_response = None
    
    def conversation_continue(self, messages, temperature=0):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=temperature
        )
        sql_response = response.choices[0].message['content']

        return sql_response

    def add_prompts_conversation(self, _):
        #Get the value introduced by the user
        prompt = client_prompt.value_input
        client_prompt.value = ''
        
        #Append to the context the User promnopt. 
        context.append({'role':'user', 'content':f"{prompt}."})
        context.append({'role':'system', 'content':f"Remember your instructions as SQL Assistant."})
        
        #Get the response. 
        response = self.conversation_continue(context)
        
        #Add the response to the context. 
        context.append({'role':'assistant', 'content':f"{response}"})
        
        # Extract the sql from the response.
        self.last_sql_response = response.split("this is your SQL,")[1].strip()
        
        #Undate the panels to show the conversation. 
        panels.append(
            pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
        panels.append(
            pn.Row('Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))
    
        return pn.Column(*panels)
    
    def run_sql_query(self, _):
        db_results = None
        if self.last_sql_response:
            try:
                self.sql_db_ops.connect()
                conn = self.sql_db_ops.get_db_connection()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute(self.last_sql_response)
                db_results = cursor.fetchall()
                cursor.close()
                self.sql_db_ops.close_connection()
            except pymysql.Error as e:
                if cursor:
                    cursor.close()
                self.sql_db_ops.close_connection()
                print(f"Database error: {str(e)}")

            if isinstance(db_results, list) and db_results and isinstance(db_results[0], dict):
                df = pd.DataFrame(db_results)
                panels.append(pn.Row('DB Results:', pn.pane.DataFrame(df, width=600, styles={'background-color'})))
        
        
app = SQLApp()
pn.extension()
panels = []
client_prompt = pn.widgets.TextInput(value="Hi", placeholder='Order your data…')
button_conversation = pn.widgets.Button(name="generate SQL")
interactive_conversation = pn.bind(app.add_prompts_conversation, button_conversation)
dashboard = pn.Column(
    client_prompt,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)
dashboard.servable()