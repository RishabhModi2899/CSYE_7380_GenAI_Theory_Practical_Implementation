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
  "tableName": "employees",
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
  "tableName": "employees",
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
      "name": "",
      "type": "STRING"
    }
  ]
}
"""
})