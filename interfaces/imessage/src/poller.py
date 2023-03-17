import polling
from .receive import get_new_messages_from_user


def main():
    polling.poll(
        lambda: print(get_new_messages_from_user()),
        step=5,
        poll_forever=True)
