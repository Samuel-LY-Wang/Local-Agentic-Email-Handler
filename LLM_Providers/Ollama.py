from LLM_Providers.LLM_Provider import Base_LLM_Provider
from Constants.Base_Sys_Prompt import BASE_SYS_PROMPT
import ollama

class Ollama(Base_LLM_Provider):
    def __init__(self):
        pass # no params needed, just need the base class for polymorphism anyways

    def authenticate(self) -> bool:
        """
        Ollama does not require authentication, so this method always returns True.
        """
        return True

    def invoke(self, model: str, in_context: str) -> str:
        """
        This is the method to invoke an Ollama model.
        """
        try:
            resp = ollama.chat(model=model, messages=[{"role": "system", "content": BASE_SYS_PROMPT}, {"role": "user", "content": in_context}])
            return resp['content']
        except ollama.ResponseError as e:
            raise Exception(f"Error invoking Ollama model: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred while invoking Ollama model: {e}")