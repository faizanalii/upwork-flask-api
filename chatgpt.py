import openai
from typing import List, Dict

MODEL: str = "gpt-4-0613"

"""
Get the response for query asked
"""


def get_query_response(prompt: str, chatgpt_key: str) -> str:
    openai.api_key = chatgpt_key
    chatgpt_connection = openai

    completion: Dict = chatgpt_connection.ChatCompletion.create(
        model=MODEL, messages=[{"role": "user", "content": prompt},],
    )

    query_response: str = completion.get("choices", [])[0].get("message", {}).get(
        "content", prompt
    )

    return query_response
