from typing import Any, List, Optional

import requests

from langchain_core.language_models.llms import LLM


class KaggleLLM(LLM):

    endpoint_url: str

    api_key: str

    max_new_tokens: int = 500

    timeout: int = 180

    ##########################################################

    def _call(

        self,

        prompt: str,

        stop: Optional[List[str]] = None,

        **kwargs: Any

    ) -> str:

        response = requests.post(

            f"{self.endpoint_url}/generate",

            headers={

                "Authorization": f"Bearer {self.api_key}"

            },

            json={

                "prompt": prompt,

                "max_new_tokens": self.max_new_tokens

            },

            timeout=self.timeout

        )

        response.raise_for_status()

        return response.json()["text"]

    ##########################################################

    @property
    def _llm_type(self):

        return "kaggle_mistral"
    @staticmethod
    def get_llm(endpoint_url, api_key, max_new_tokens=300):
        return KaggleLLM(
            endpoint_url=endpoint_url,
            api_key=api_key,
            max_new_tokens=max_new_tokens
        )