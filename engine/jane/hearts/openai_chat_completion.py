from typing import Tuple
from ..types import History
import openai
openai.api_key_path = "openai_api_key.txt"


def init_history() -> History:
    return [{"role": "system", "content": "you are a helpful, intelligent, and fallible digital personal assistant"}]


def generate(input: str, history: History) -> Tuple[str, History]:
    history += [{"role": "user", "content": input}]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )
    history += [completion.choices[0].message]
    return history[-1].content, history
