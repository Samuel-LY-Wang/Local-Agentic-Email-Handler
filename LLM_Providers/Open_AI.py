import os
from LLM_Providers.LLM_Provider import Base_LLM_Provider
from Constants.Base_Sys_Prompt import BASE_SYS_PROMPT
from openai import OpenAI

class Open_AI(Base_LLM_Provider):
    def __init__(self, API_key: str = ""):
        super().__init__(name="OpenAI", endpoint="https://api.openai.com/v1", API_key=API_key)
        resolved_API_key = self.API_key if self.API_key else os.environ.get("OPENAI_API_KEY")
        if (not resolved_API_key):
            raise ValueError("OpenAI API key must be provided either as a parameter or through the OPENAI_API_KEY environment variable.")
        self.client = OpenAI(api_key=resolved_API_key)
        pass # no params needed, just need the base class for polymorphism anyways

    def authenticate(self) -> bool:
        """
        This method checks if the OpenAI API key is valid by making a simple request to the OpenAI API.
        """
        try:
            # Attempt to list models as a way to check if the API key is valid
            self.client.models.list()
            return True
        except Exception as e:
            return False

    def invoke(self, model: str, in_context: str) -> str:
        """
        This is the method to invoke an OpenAI model.
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": BASE_SYS_PROMPT},
                    {"role": "user", "content": in_context}
                ]
            )
            msg = response.choices[0].message.content
            return msg if msg else ""
        except Exception as e:
            raise Exception(f"Error invoking OpenAI model: {e}")