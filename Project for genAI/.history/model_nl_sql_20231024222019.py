import openai
import os
from dotenv import load_dotenv
import panel as pn

load_dotenv()

openai.api_key=os.environ.get('openai_key')


def add_prompts_conversation():
    prompt = client_prompt.value_input

def conversation_continue(messages, temperature=0):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message['content']

pn.extension()
panels = []
client_prompt = pn.widgets.TextInput(value="Hi", placeholder='Order your data…')
button_conversation = pn.widgets.Button(name="generate SQL")
interactive_conversation = pn.bind(add_prompts_conversation, button_conversation)
dashboard = pn.Column(
    client_prompt,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)
print(dashboard)
