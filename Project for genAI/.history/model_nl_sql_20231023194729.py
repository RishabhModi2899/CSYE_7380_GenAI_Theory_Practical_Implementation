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
    return response.choices[0]