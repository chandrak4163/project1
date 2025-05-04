import os
from dotenv import load_dotenv
from openai import OpenAI  # Correct import for SDK v1+

# Load API key from .env
load_dotenv()
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=OpenAI_Key)

# Get user input
topic = input("Enter the topic: ")

# Define messages for GPT
messages = [
    {"role": "system", "content": "You explain the concept of the given topic clearly and simply."},
    {"role": "user", "content": f'Demonstrate the topic:\n\n"{topic}"'}
]

# Call the GPT-4o model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

# Extract and print the result
topic_description = response.choices[0].message.content.strip()
print(f"\nExplanation of '{topic}':\n{topic_description}")
