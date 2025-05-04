from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Sample Resume
resume = """
Name: John Doe
Role: Python Developer
Experience: 3 years at TechSoft Inc.
Skills: Python, Django, REST APIs, SQL
Projects: Built scalable backend for e-commerce, improved API response by 30%
"""

# Role-based prompt
role_based_prompt = "You are a hiring manager reviewing a resume for a backend Python developer. Provide constructive feedback."
generic_prompt = "Evaluate this resume."

# Run both prompts
for label, prompt in [("Role-Based", role_based_prompt), ("Generic", generic_prompt)]:
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Resume:\n{resume}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0
    )
    print(f"\n--- {label} Prompt ---")
    print("Prompt:", prompt)
    print("Output:", response.choices[0].message.content.strip())
