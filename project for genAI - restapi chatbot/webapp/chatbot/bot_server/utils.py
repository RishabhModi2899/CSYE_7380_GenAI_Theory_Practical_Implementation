from openai import OpenAI, OpenAIError
from django.db import DatabaseError, connection
from django.conf import settings


def analyze_request_with_openai(user_input):
    if not user_input or not isinstance(user_input, str):
        raise ValueError("User input must be a non-empty string.")

    try:
        client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
        context = '''
                    You are an AI assistant.
                    The context of the database information is as follows:
                    The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics tracks the on-time performance of domestic flights operated by large air carriers.
                    Summary information on the number of on-time, delayed, canceled, and diverted flights is published in DOT's monthly Air Travel Consumer Report and in this dataset of 2015 flight delays and cancellations.
                    Based on the information you need to determine, if the user request is asking for information from a database or if it's a general knowledge question.
                    Response should be 'database' for database queries, 'general' for all other requests.
                '''
        message = [
            {"role": "system", "content": context
             },
            {"role": "user", "content": user_input},
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message,
            max_tokens=10,
            temperature=0
        )

        # Extracting the response and classifying it
        classification = response.choices[0].message.content.lower()
        # Basic validation of the classification
        if classification in ['database', 'general']:
            return classification
        else:
            raise ValueError("Invalid classification received from OpenAI.")
    except OpenAIError as e:
        raise ValueError(f"OpenAI API error: {e}")


def generate_sql_with_openai(user_input):
    context = [{'role': 'system', 'content': """
    Your Database is composed by a SQL database with some tables. \
    Try to Maintain the SQL order simple.
    Put the SQL command in white letters with a black background, and just after \
    a simple and concise text explaining how it works. 
    If the user ask for something that can not be solved with an SQL Order \
    just answer something nice and simple and ask him for something that \
    can be solved with SQL. 
    """}]

    context.append({'role': 'system', 'content': """
        first table: 
        {
        "tableName": "bot_server_airline",
        "fields": [{
            "name": "id",
            "type": "int"
            },
            {
            "name": "iata_code",
            "type": "string"
            },
            {
            "name": "airline",
            "type": "string"
        }],
        "primaryKey": "id",
        "relations": []
        }
        """
                    })

    context.append({'role': 'system', 'content': """
        second table: 
        {
        "tableName": "bot_server_airport",
        "fields": [{
            "name": "id",
            "type": "int"
            },
            {
            "name": "iata_code",
            "type": "string"
            },
            {
            "name": "city",
            "type": "string"
            },
            {
            "name": "state",
            "type": "string"
            },
            {
            "name": "country",
            "type": "string"
            },
            {
            "name": "latitude",
            "type": "float"
            },
            {
            "name": "longitude",
            "type": "float"
            },
        ]},
        "primaryKey": "id",
        "relations": []
        """
                    })

    context.append({'role': 'system', 'content': """
    third table: 
    {
    "tablename": "bot_server_flight",
    "fields": [{
        "name": "id",
        "type": "int"
        },
        {
        "name": "year",
        "type": "int"
        },
        {
        "name": "month",
        "type": "int"
        },
        {
        "name": "day",
        "type": "int"
        },
        {
        "name": "day_of_week",
        "type": "int"
        },
        {
        "name": "airline",
        "type": "string"
        },
        {
        "name": "flight_number",
        "type": "int"
        },
        {
        "name": "tail_number",
        "type": "string"
        },
                {
        "name": "origin_airport",
        "type": "string"
        },
                        {
        "name": "destination_airport",
        "type": "string"
        },
                                {
        "name": "scheduled_departure",
        "type": "int"
        },
                                        {
        "name": "departure_time",
        "type": "int"
        },
                                                {
        "name": "departure_delay",
        "type": "int"
        },
                                                        {
        "name": "taxi_out",
        "type": "int"
        },
                                                                {
        "name": "wheels_off",
        "type": "int"
        },
                                                                        {
        "name": "scheduled_time",
        "type": "string"
        },
                                                                                {
        "name": "elapsed_time",
        "type": "int"
        },
                                                                                        {
        "name": "air_time",
        "type": "int"
        },
                                                                                                {
        "name": "distance",
        "type": "int"
        },
                                                                                                        {
        "name": "wheels_on",
        "type": "int"
        },
                                                                                                                {
        "name": "taxi_in",
        "type": "int"
        },
                                                                                                                        {
        "name": "scheduled_arrival",
        "type": "int"
        },
                                                                                                                                {
        "name": "arrival_time",
        "type": "int"
        },
                                                                                                                                        {
        "name": "arrival_delay",
        "type": "int"
        },
                                                                                                                                                {
        "name": "diverted",
        "type": "int"
        },
                                                                                                                                                        {
        "name": "cancelled",
        "type": "int"
        },
                                                                                                                                                                {
        "name": "cancellation_reason",
        "type": "string"
        },
                                                                                                                                                                        {
        "name": "air_system_delay",
        "type": "int"
        },
           {
        "name": "security_delay",
        "type": "int"
        },
                   {
        "name": "airline_delay",
        "type": "int"
        },
                           {
        "name": "late_aircraft_delay",
        "type": "int"
        },
                                   {
        "name": "weather_delay",
        "type": "int"
        },
    ]},
    "primaryKey": "id",
    "relations": [
        {
            "type": "FK",
            "field": "airline",
            "references": {
                "table": "bot_server_airline",
                "field": "iata_code"
                }
        },
        {
            "type": "FK",
            "field": "origin_airport",
            "references": {
                "table": "bot_server_airport",
                "field": "iata_code"
                }
        },
        {
            "type": "FK",
            "field": "destination_airport",
            "references": {
                "table": "bot_server_airport",
                "field": "iata_code"
                }
        }
    ]
    """
                    })

    if not user_input or not isinstance(user_input, str):
        raise ValueError("User input must be a non-empty string.")

    try:
        client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        context.append({'role': 'user', 'content': f"{user_input}."})
        context.append(
            {'role': 'system', 'content':
             '''
                Response that is to be generated is a SQL query, no need to give query related explanation. Remember to add a semi-colon at the end of the sql query.
                Remember your instructions as SQL Assistant.
            '''})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=context,
            max_tokens=150,
            temperature=0
        )

        # The response is expected to contain a SQL query
        sql_query = response.choices[0].message.content

        # Basic validation of the SQL could be added here
        processed_sql = process_sql_query(sql_query)

        return processed_sql
    except OpenAIError as e:
        raise ValueError(f"OpenAI API error: {e}")


def process_sql_query(sql_query):
    sql_query_tokens = sql_query.split('\n')
    flag = False
    res = []
    for token in sql_query_tokens:
        for i in token.split():
            if i == 'SELECT':
                flag = True
                res.append(i)
            elif ';' in i:
                flag = False
                res.append(i)
                break
            elif flag:
                res.append(i)

    return ' '.join(res)


def execute_sql_query(sql_query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
    except DatabaseError as e:  # Catch Django's database-related exceptions
        raise ValueError(f"Database error: {e}")
    except Exception as e:  # Catch other unforeseen exceptions
        raise ValueError(f"Unexpected error occurred: {e}")


def handle_openai_request(user_input):
    try:
        client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        raise ValueError(f"OpenAI API error: {e}")
