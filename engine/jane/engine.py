
from typing import List, Dict
from .hearts.openai_chat_completion import generate, init_history


def invoke_tool():
    return


History = List[Dict[str, str]]
history = init_history()


def step(user_input: str) -> str:
    """takes in input, puts out response/output after doing an evaluation step (including tool invocation)"""
    global history
    response = generate(history, user_input)
    history += [{"role": "assistant", "content": response}]
    # TODO loop and invoke tools if appropriate here
    return response
