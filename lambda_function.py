import os
import json
import requests

def lambda_handler(event, context):
    # Get Groq API key from environment
    groq_api_key = os.environ.get('GROQ_API_KEY')
    if not groq_api_key:
        return {"statusCode": 500, "body": "Missing GROQ_API_KEY env variable"}

    # Get context from event
    user_context = event.get('context', 'Hello, Groq!')

    # Prepare Groq API request (sample for chat/completions)
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_context}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=15)
        response.raise_for_status()
        groq_result = response.json()
    except Exception as e:
        return {"statusCode": 500, "body": f"Groq API call failed: {str(e)}"}

    # Print and return the Groq response
    print("Groq API response:", groq_result)
    return {
        "statusCode": 200,
        "body": json.dumps(groq_result)
    } 