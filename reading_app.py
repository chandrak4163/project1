import os
from dotenv import load_dotenv
from openai import OpenAI  # correct import for the new SDK

# Load API key from .env
load_dotenv()
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Initialize client
client = OpenAI(api_key=OpenAI_Key)

# Get input text
review = input("Enter the input: ")

# Choose task: grammar correction
messages = [
    {"role": "system", "content": "You correct grammar and spelling in English text."},
    {"role": "user", "content": f'Correct the following text:\n\n"{review}"\n\nCorrected:'}
]

# Call GPT-4o model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

# Output the result
correction = response.choices[0].message.content.strip()
print(f"Corrected response: {correction}")
