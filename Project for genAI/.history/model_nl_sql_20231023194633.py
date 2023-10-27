import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.environ.get('openai_key')

def conversation_continue(messages, temperature=0):
    response = openai.