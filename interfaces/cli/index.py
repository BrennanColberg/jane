import requests

API_ROOT = "http://localhost:4000"


def main():
    input_string = input("you: ")
    response = requests.post(f"{API_ROOT}/step", data=input_string).json()
    session_id = response["session_id"]
    print("session_id=" + session_id)
    print("jane: " + response["output"])
    while True:
        input_string = input("you: ")
        response = requests.post(
            f"{API_ROOT}/step/{session_id}", data=input_string).json()
        print("jane: " + response["output"])


if __name__ == "__main__":
    main()
