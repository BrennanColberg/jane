import polling
from .receive import get_new_messages


def main():
    polling.poll(
        lambda: print(get_new_messages()),
        step=5,
        poll_forever=True)
