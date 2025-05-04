"""""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client (new SDK style)
client = OpenAI(api_key=OpenAI_Key)

# Get review input
review = input("Enter the input: ")

# Prepare prompt messages
messages = [
    {"role": "system", "content": "You classify restaurant review sentiment as Positive, Negative, or Neutral."},
    {"role": "user", "content": f'Classify the sentiment of this review:\n\n"{review}"\n\nSentiment:'}
]

# Call GPT-4o using the new API
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

# Extract sentiment result
sentiment = response.choices[0].message.content.strip()
print(f"Corrected response: {sentiment}")
"""""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file and get the API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with your key
client = OpenAI(api_key=api_key)

# Ask the user for a restaurant review
review = input("Enter the input: ")

# Prepare messages for GPT
messages = [
    {"role": "system", "content": "You classify restaurant review sentiment as Positive, Negative, or Neutral."},
    {"role": "user", "content": f'Classify the sentiment of this review:\n\n"{review}"\n\nSentiment:'}
]

# Get the sentiment classification
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

# Display the result
sentiment = response.choices[0].message.content.strip()
print(f"Corrected response: {sentiment}")
