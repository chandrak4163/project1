import os
from dotenv import load_dotenv
from openai import OpenAI  # Use this from the new SDK

# Load environment variables from .env
load_dotenv()
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set up the client using the new SDK structure
client = OpenAI(api_key=OpenAI_Key)

def chatbot():
    print("Chatbot: Hello! Ask me anything. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        # Make a request to GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ],
            temperature=0
        )
        
        # Output the assistant's response
        print("Chatbot:", response.choices[0].message.content.strip())

# Run the chatbot
chatbot()
