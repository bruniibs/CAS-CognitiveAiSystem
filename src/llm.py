import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# show error message if GEMINI_API_KEY is not set.
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set. Please set it in your .env file."
        )

client = genai.Client(api_key=api_key)

def ask_llm(message, previous_interaction_id=None):
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=message,
        previous_interaction_id=previous_interaction_id
    )
    return interaction.output_text, interaction.id