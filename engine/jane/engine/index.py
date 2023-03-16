
from ..hearts.openai_chat_completion import generate, init_history


def invoke_tool():
    return


def main():
    history = init_history()
    while (True):
        user_input = input('You: ')
        response = generate(history, user_input)
        print(f"Jane: {response}")
        history += [{"role": "assistant", "content": response}]

    # initial_prompt = f"Digital Personal Assistant: {user_input}\n"

    # prompt = initial_prompt
    # while True:
    #     response = generate(prompt)
    #     if response.lower() == "done":
    #         break
    #     elif response.startswith("use tool:"):
    #         tool_name = response[len("use tool:"):].strip()
    #         tool_output = invoke_tool(tool_name)
    #         prompt += f"\n{tool_output}\n"
    #     else:
    #         print(f"Unexpected response: {response}")
    #         break

    print("Process completed.")


if __name__ == "__main__":
    main()
