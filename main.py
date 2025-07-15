import os
from dotenv import load_dotenv
from agent.response_generator import get_response

load_dotenv()

print("Welcome to Bangalore Smart Agent! Type 'exit' to quit.")
chat_history = []

while True:
    user_input = input("\nUser: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response, persona = get_response(user_input, chat_history)
    chat_history.append((user_input, response))
    print(f"\nAgent ({persona}): {response}")
