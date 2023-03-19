from uuid import uuid4
from typing import Tuple
from .history import get_history, save_history
from .types import History
from .hearts.openai_chat_completion import generate


def invoke_tool():
    return


def step(session_id: str, user_input: str) -> Tuple[str, History]:
    """takes in input, puts out response/output after doing an evaluation step (including tool invocation)"""
    if user_input.startswith("/new"):
        user_input = user_input[5:]
        session_id = uuid4()
    history = get_history(session_id)
    response, history = generate(user_input, history)
    # TODO loop and invoke tools if appropriate here
    save_history(session_id, history)
    return response, history
