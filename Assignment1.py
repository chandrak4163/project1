from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


article = """
NASA will launch a flagship mission in 2031 to explore Uranus and Neptune. 
This mission will be the first to closely study the atmospheres, moons, 
and magnetic fields of the two ice giants, aiming to expand our understanding 
of how these distant planets formed and evolved over billions of years.
"""

# Define 3 prompts
prompts = [
    "Summarize the article.",
    "Summarize the key scientific goals of NASA’s new mission to Uranus and Neptune in simple terms.",
    "Give a 3-sentence summary of the article highlighting (1) the mission timeline, (2) key scientific goals, and (3) why this mission matters."
]

# Run each prompt
for i, prompt_text in enumerate(prompts, start=1):
    messages = [
        {"role": "system", "content": "You are a helpful summarizer."},
        {"role": "user", "content": f"{prompt_text}\n\nArticle:\n{article}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    print(f"\n--- Prompt {i} ---")
    print(f"Prompt: {prompt_text}")
    print("Output:", response.choices[0].message.content.strip())
