from typing import NamedTuple


class Message(NamedTuple):
    id: int
    text: str
    date: int
    from_address: str
    to_address: str
