import os
import lambda_function
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Set a dummy Groq API key only if not set in the environment
if not os.environ.get('GROQ_API_KEY'):
    os.environ['GROQ_API_KEY'] = 'sk-xxx-your-groq-key-here'

event = {
    'context': 'Tell me a joke about AI.'
}

result = lambda_function.lambda_handler(event, None)
print('Lambda result:')
print(result) 