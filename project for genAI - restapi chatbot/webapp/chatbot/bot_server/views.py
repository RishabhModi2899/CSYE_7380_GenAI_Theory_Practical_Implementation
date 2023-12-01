import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bot_server.utils import analyze_request_with_openai, generate_sql_with_openai, execute_sql_query, handle_openai_request


@csrf_exempt
def handle_user_request(request):
    if request.method == "POST":
        try:
            # Parse the JSON from the request body
            data = json.loads(request.body)
            user_input = data.get('user_input')

            # Proceed with handling the user input...
            # Determine the type of request with OpenAI
            classification = analyze_request_with_openai(user_input)

            if classification == 'database':
                # Generate SQL with OpenAI
                sql_query = generate_sql_with_openai(user_input)
                # Execute the SQL query and fetch data from the database
                data = execute_sql_query(sql_query)
                response_data = {'data': data}
            else:
                # Handle general response with OpenAI
                response_data = {'data': handle_openai_request(user_input)}
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except ValueError as e:
            response_data = {'error': str(e)}
        
        return JsonResponse(response_data, safe=False)
