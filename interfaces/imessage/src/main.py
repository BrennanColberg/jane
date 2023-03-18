import polling
from .receive import get_new_messages_from_user
from .send import send_message_to_user
import requests
import os


session_id = None
api_root = os.environ["API_ROOT"]


def handle_new_message_from_user(new_message: str):
    try:
        global session_id
        api_endpoint = "/step" if session_id is None else f"/step/{session_id}"
        response = requests.post(api_root + api_endpoint, data=new_message)
        response_json = response.json()
        session_id = response_json["session_id"]
        output = response_json["output"]
        send_message_to_user(output)
    except Exception as e:
        print("Error handling new message from user: ", e)
        send_message_to_user("❌ Error while responding:" + "\n\n" + str(e))


def check_for_new_messages_from_user():
    for new_message in get_new_messages_from_user():
        print("new message from user: ", new_message)
        handle_new_message_from_user(new_message)


def poll():
    polling.poll(check_for_new_messages_from_user, step=1, poll_forever=True)
