import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(api_key=api_key)

prompt = "What is Artificial Intelligence? Explain in simple words."

for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        print("\nGemini AI Response:")
        print(response.text)
        break

    except Exception as error:
        print(f"Attempt {attempt + 1} failed: {error}")

        if attempt < 2:
            wait = 5 * (2 ** attempt)
            print(f"Retrying in {wait} seconds...")
            time.sleep(wait)
        else:
            print("Gemini is currently unavailable. Try again later.")