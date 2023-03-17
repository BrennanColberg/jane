import sqlite3
import os
from .types import Message

imessage_db_path = os.path.expanduser("~/Library/Messages/chat.db")


def _extract_text(attributed_body: bytes):
    # adapted from
    attributed_body = attributed_body.decode('utf-8', errors='replace')
    if "NSNumber" in str(attributed_body):
        attributed_body = str(attributed_body).split("NSNumber")[0]
        if "NSString" in attributed_body:
            attributed_body = str(attributed_body).split("NSString")[1]
            if "NSDictionary" in attributed_body:
                attributed_body = str(
                    attributed_body).split("NSDictionary")[0]
                attributed_body = attributed_body[6:-12]
                return attributed_body
    return None


def _message_from_row(row) -> Message:
    id, body, text, date, with_address, is_from_me = row
    me = None
    message = Message(id=id,
                      text=text if text else _extract_text(body),
                      date=date,
                      from_address=with_address if not is_from_me else me,
                      to_address=with_address if is_from_me else me)
    return message


def get_recent_messages(num: int) -> list[Message]:
    connection = sqlite3.connect(imessage_db_path)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT m.ROWID, m.attributedBody, m.text, m.date, h.id, m.is_from_me
        FROM message m
        LEFT JOIN handle h ON m.handle_id = h.ROWID
        ORDER BY m.date DESC
        LIMIT ?;
        """, (num))
    rows = cursor.fetchall()
    connection.close()
    return [_message_from_row(row) for row in rows]


seen_message_ids = None


def init_seen_message_ids():
    global seen_message_ids
    seen_message_ids = set()
    for message in get_recent_messages():
        seen_message_ids.add(message.id)


def get_new_messages() -> list[Message]:
    global seen_message_ids
    if (seen_message_ids is None):
        init_seen_message_ids()
    new_messages = [m for m in get_recent_messages()
                    if m.id not in seen_message_ids]
    for message in new_messages:
        seen_message_ids.add(message.id)
    return new_messages
