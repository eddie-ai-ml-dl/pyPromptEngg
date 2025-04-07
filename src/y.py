from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
prompt = "What's the weather like in London?"

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt)

print(response.text)

def get_current_weather(location: str):
    """Gets the current weather conditions for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA

    Returns:
        A dictionary containing the temperature(e.g. 70), unit, feels_like (e.g. 65), condition(e.g. cloudy), humidity and wind_speed.
    """

    return {
        "location": location,
        "temperature": 61.0,
        "unit": "fahrenheit",
        "feels_like": 61.0,
        "condition": "Partly cloudy",
        "humidity": 30,
        "wind_speed": "2.2 mph"
    }

config = types.GenerateContentConfig(
    tools=[get_current_weather]
)  # Pass the function itself

# Make the request
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=config,
)

print("FUNCTION CALLING:", response.text)