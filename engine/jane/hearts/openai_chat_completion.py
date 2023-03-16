import openai
openai.api_key_path = "openai_api_key.txt"


def init_history() -> list[dict[str, str]]:
    return [{"role": "system", "content": "you are a helpful, intelligent, and fallible digital personal assistant"}]


def generate(history: list[dict[str, str]], input: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history + [{"role": "user", "content": input}]
    )
    return completion.choices[0].message.content
