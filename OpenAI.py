from openai import OpenAI
import openai
import os
import base64


class OpenAIWrapper:
    def __init__(self):

        os.environ["OPENAI_API_KEY"] = "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"
        openai.api_key = "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"
        self.client = OpenAI()


    def chat_completion(self, messages: list, model="gpt-4", temperature=0.7):
        """
        Uses OpenAI's chat completion endpoint.

        Args:
            messages (list): A list of dictionaries representing the chat history.
            model (str): The model to use (default is gpt-4).
            temperature (float): Sampling temperature to control randomness.

        Returns:
            dict: The API response.
        """
        completion = self.client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "user", "content": messages}
            ]
        )
        return completion
