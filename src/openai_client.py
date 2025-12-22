import os
import time
try:
    from dotenv import load_dotenv
except ImportError:
    # Fallback if python-dotenv is not installed; environment variables must already be set
    def load_dotenv(*args, **kwargs):
        return False
from openai import OpenAI

# Load environment variables
load_dotenv()

# Default configuration
DEFAULT_MODEL = "gpt-4o-mini"

def get_client():
    """
    Creates and returns an OpenAI Client.
    Ensures the API key is available in the environment.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API Key not found. Please set OPENAI_API_KEY in your .env file.")
    
    return OpenAI(api_key=api_key)

def get_model(): 
    """
    Returns the default model name.
    """
    return DEFAULT_MODEL

def list_models():
    """
    Returns a sorted list of all available model IDs from OpenAI.
    """
    client = get_client()
    try:
        models = client.models.list()
        ids = [m.id for m in models.data]
        return sorted(ids)
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

def list_text_models():
    """
    Returns a filtered list of models suitable for text/chat generation.
    Excludes embedding, audio, image-only, and TTS models.
    """
    ids = list_models()
    if not ids:
        return []

    exclude_keywords = [
        "embedding", "audio", "whisper", "tts", "speech", "image", "clip"
    ]
    def is_text_model(mid: str) -> bool:
        lower = mid.lower()
        if any(k in lower for k in exclude_keywords):
            return False
        # Common families for text/chat
        return lower.startswith("gpt") or lower.startswith("o") or lower.startswith("text-")

    return [mid for mid in ids if is_text_model(mid)]

def generate_text(prompt, model_name=DEFAULT_MODEL, system_instruction=None, temperature=0.7):
    """
    Generates text from a prompt using the specified model.
    
    Args:
        prompt (str): The input text prompt.
        model_name (str): The name of the model to use (default: gpt-4o-mini).
        system_instruction (str): Optional system instructions to guide the model.
        temperature (float): Controls randomness (0.0 to 1.0).
    
    Returns:
        str: The generated text.
    """
    client = get_client()
    
    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating text: {e}")
        return None

def generate_text_stream(prompt, model_name=DEFAULT_MODEL, system_instruction=None, temperature=0.7):
    """
    Generates text in a stream (yields chunks).
    """
    client = get_client()
    
    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})
    
    try:
        stream = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature,
            stream=True
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
    except Exception as e:
        print(f"Error in streaming: {e}")

class Chat:
    """
    A class to manage chat history and state, similar to Gemini's ChatSession.
    """
    def __init__(self, model_name=DEFAULT_MODEL, system_instruction=None, history=None):
        self.client = get_client()
        self.model_name = model_name
        self.messages = []
        
        if system_instruction:
            self.messages.append({"role": "system", "content": system_instruction})
        
        if history:
            self.messages.extend(history)

    def send_message(self, message):
        """
        Sends a message to the model and returns the response text.
        Appends both user message and assistant response to history.
        """
        self.messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.messages
            )
            reply = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            print(f"Error sending message: {e}")
            return None

def chat_session(model_name=DEFAULT_MODEL, system_instruction=None):
    """
    Starts a simple interactive chat session in the terminal.
    """
    chat = Chat(model_name, system_instruction)
    
    print(f"--- Chat Session Started ({model_name}) ---")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        
        response = chat.send_message(user_input)
        if response:
            print(f"OpenAI: {response}")

if __name__ == "__main__":
    print("--- Testing OpenAI API ---")
    
    # 1. Simple Text Generation
    print("\n1. Simple Text Generation:")
    result = generate_text("Explain quantum computing in one sentence.")
    print(f"Result: {result}")
    
    # 2. System Instructions
    print("\n2. With System Instructions (Pirate Mode):")
    pirate_result = generate_text(
        "Hello, how are you?", 
        system_instruction="You are a pirate. Speak like one."
    )
    print(f"Result: {pirate_result}")
    
    # 3. Streaming
    print("\n3. Streaming Response:")
    print("Result: ", end="", flush=True)
    for chunk in generate_text_stream("Count to 5 slowly."):
        print(chunk, end="", flush=True)
    print()
    
    # 4. Chat Session (Uncomment to run interactively)
    # chat_session()
