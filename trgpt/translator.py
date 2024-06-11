import os
import yaml
from openai import OpenAI


class Translator:
    def __init__(self, config_path: str) -> None:
        """
        Initializes the Translator with the configuration file.
        """
                
        self.config: dict = self.load_config(config_path)                                   # Loading configuration from the file
        self.client: OpenAI = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))              # Initializing the OpenAI client with the API key from environment variables
        self.model_name: str = self.config['model_name']                                    # Getting the model name from the configuration
        self.translation_preferences: dict = self.config['translation_preferences']         # Getting translation preferences from the configuration


    def load_config(self, config_path: str) -> dict:
        """
        Loads the configuration from a YAML file.

        Args:
            config_path (str): Path to the configuration file.

        Returns:
            dict: The loaded configuration.
        """
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
        

    def translate(self, text: str) -> dict[str, str]:
        """
        Translates the given text based on the configuration.

        Args:
            text (str): Text to be translated.

        Returns:
            dict[str, str]: The translated text.
        """

        translations: str = ''
        
        system_prompt: str = f"""
        You are a translator application. 
        
        Provide concise translations from the identified language to one or several languages specified in {self.translation_preferences} for the source language. 
        If no target language for source language specified, you should choose target language by yourself. If appropriate you should choose target languages for other source languages.
              
        If there are several targeted languages for the source language, you should divide translations by row that consists from '---Translation to <targeted language>---'. 
        
        Determine the source language automatically. If input makes no sense or you can't detect the source language you should return phrase: "Sorry, i can't identify the inputed language.".
        If language could be identified but there are some mistakes, you should make translation with fixed mistakes
        """
        response: dict = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        )

        translations = response.choices[0].message.content                                  # Extracting the translation from the API response
        return translations
