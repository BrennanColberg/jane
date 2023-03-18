import json
import os
from .hearts.openai_chat_completion import init_history
from .types import History


history_cache: dict[str, History] = {}


def get_history(session_id: str) -> History:
    """get history from ram dict or from json file"""
    global history_cache
    if session_id in history_cache:
        return history_cache[session_id]
    else:
        file_path = f"./history/{session_id}.jsonl"
        # If the file doesn't exist, initialize history
        if not os.path.exists(file_path):
            history = init_history()
        else:
            # Read from JSON file at ./history/{session_id}.json
            with open(file_path, "r") as file:
                history = []
                for line in file:
                    json_obj = json.loads(line.strip())
                    history.append(json_obj)
        history_cache[session_id] = history
        return history


def save_history(session_id: str, history: History):
    """save history to ram dict and to json file"""
    global history_cache
    history_cache[session_id] = history
    # write to json file at ./history/{session_id}.json
    with open(f"./history/{session_id}.jsonl", "w") as file:
        for json_obj in history:
            line = json.dumps(json_obj)
            file.write(line + '\n')


def add_to_history(session_id: str, role: str, content: str):
    """add a new entry to the history"""
    history = get_history(session_id)
    history.append({"role": role, "content": content})
    save_history(session_id, history)
