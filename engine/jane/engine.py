
from typing import Tuple
from .history import History
from .hearts.openai_chat_completion import generate, init_history


def invoke_tool():
    return


history = init_history()


def step(user_input: str) -> Tuple[str, History]:
    """takes in input, puts out response/output after doing an evaluation step (including tool invocation)"""
    global history
    response, history = generate(user_input, history)
    # TODO loop and invoke tools if appropriate here
    return response, history
