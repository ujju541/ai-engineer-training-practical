import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# System prompt
SYSTEM_PROMPT = """
You are an internal IT support assistant.

Your job is to help employees with common IT problems such as:
- Wi-Fi problems
- Laptop problems
- Password issues
- VPN problems
- Software installation

Be professional, clear, concise, and helpful.

If you are not sure about something, clearly say that you are not sure.
"""

print("===================================")
print("   Internal IT Support Chatbot")
print("===================================")
print("Type 'exit' to quit.\n")


while True:

    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_question,
        config={
            "system_instruction": SYSTEM_PROMPT
        }
    )

    print("\nAI:", response.text)
    print()