import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_prompt = "You are an internal IT support assistant."

user_question = "My laptop is not connecting to Wi-Fi."

# Request data
request_data = {
    "model": "gemini-2.5-flash",
    "system_instruction": system_prompt,
    "user_message": user_question
}

print("========== REQUEST JSON ==========")
print(json.dumps(request_data, indent=4))


# LLM call
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_question,
    config={
        "system_instruction": system_prompt
    }
)

# Response data
response_data = {
    "text": response.text
}

print("\n========== RESPONSE JSON ==========")
print(json.dumps(response_data, indent=4))