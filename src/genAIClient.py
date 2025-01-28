# generative_ai_utils.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

class GenerativeAIClient:
    """
    A client for interacting with Google's Generative AI models.  Configures the API
    on initialization and provides a method to invoke the model and return the text response.
    """

    def __init__(self, api_key=None, model_name='gemini-pro', show_info_log=True):
        """
        Initializes the GenerativeAIClient.

        Args:
            api_key: The Google Generative AI API key. If None, it will attempt to
                     read it from the GOOGLE_API_KEY environment variable.
            model_name: The name of the generative model to use.
            show_info_log: If True, will log messages to stdout.
        """
        self.show_info_log = show_info_log
        self.api_key = api_key or os.environ.get('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("API Key not provided or found in environment.")
        self.model_name = model_name
        self.model = None  # Initialize model to None; create it lazily
        self._configure_api()
        # self._initialize_model() #Initialize model eagerly, or do it lazily when invoked

    def _configure_api(self):
        """Configures the Google Generative AI API."""
        try:
            genai.configure(api_key=self.api_key)
            if self.show_info_log:
                logging.info("Google Generative AI API configured successfully.")
        except Exception as e:
            logging.error(f"Error configuring Google Generative AI API: {e}")
            raise

    def _initialize_model(self):
         try:
            self.model = genai.GenerativeModel(self.model_name)
            if self.show_info_log:
                logging.info(f"Initialized model: {self.model_name}")
         except Exception as e:
            logging.error(f"Error initializing model {self.model_name}: {e}")
            raise

    def invoke(self, prompt, sys_instructions=None, log_token_counts=True):
        """
        Invokes the generative model with the given prompt and system instructions,
        returning the generated text.

        Args:
            prompt: The user prompt.
            sys_instructions: Optional system instructions.
            log_token_counts: Optional token counts log flag.

        Returns:
            The generated text, or None if an error occurs.
        """
        if self.model is None: #Lazy load model
            self._initialize_model()

        sys_instructions = sys_instructions or ""
        full_prompt = f"{sys_instructions}\n{prompt}"

        try:
            if self.show_info_log and log_token_counts:
                logging.info(f"Prompt Tokens: \n{self.model.count_tokens(full_prompt)}")
            response = self.model.generate_content(full_prompt)
            if response.prompt_feedback:
                logging.warning(f"Prompt feedback: {response}")
            if self.show_info_log and log_token_counts:
                logging.info(f"Token Stats: \n{response.usage_metadata}")
            return response.text
        except Exception as e:
            logging.error(f"Error invoking {self.model_name}: {e}")
            return None


if __name__ == "__main__":
    # Example Usage (after defining the functions)
    try:
        client=GenerativeAIClient(show_info_log=True)  # Instantiate the client
        system_instruction="You are a helpful AI assistant that answers questions concisely and accurately."
        user_prompt="What is the capital of France?"
        output=client.invoke(user_prompt, sys_instructions=system_instruction)
        print(f"Answer: {output}")
    except Exception as e:
        print(f"Error in chatbot: {e}")
