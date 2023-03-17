
import polling
from .receive import get_new_messages_from_user
from .send import send_message_to_user


def handle_new_message_from_user(new_message: str):
    send_message_to_user("echo: " + new_message)


def check_for_new_messages_from_user():
    for new_message in get_new_messages_from_user():
        print("new message from user: ", new_message)
        handle_new_message_from_user(new_message)


def poll():
    polling.poll(check_for_new_messages_from_user, step=1, poll_forever=True)
