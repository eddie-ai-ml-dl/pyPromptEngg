import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
print(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

DEF_MODEL = "models/gemini-2.0-flash-exp"  #'gemini-pro'

def get_model(model_name=DEF_MODEL):
    return genai.GenerativeModel(model_name)

def invoke_model(model, prompt):
    response=model.generate_content(prompt)
    return response.text
