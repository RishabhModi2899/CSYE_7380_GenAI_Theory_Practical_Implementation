import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.environ.get('openai_key')

def conversation_continue(messages, temperature=0):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message['content']

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

