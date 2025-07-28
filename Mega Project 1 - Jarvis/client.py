from openai import OpenAI
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file if available
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Set OPENAI_API_KEY in your environment or .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Request a completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the assistant's response
print(completion.choices[0].message.content)
