import sqlite3
import os

# Connect to the iMessage database
connection = sqlite3.connect(os.path.expanduser("~/Library/Messages/chat.db"))

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query
query = """
SELECT m.ROWID, m.attributedBody, m.text, m.date, h.id, m.is_from_me
FROM message m
LEFT JOIN handle h ON m.handle_id = h.ROWID
ORDER BY m.date DESC
LIMIT 30;
"""


def extract_text_from_attributed_body(attributed_body: bytes):
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


# Fetch the results
cursor.execute(query)
rows = cursor.fetchall()

# Print the results
for row in rows:
    id, attributed_body, text, date, with_address, is_from_me = row
    me = "me"
    print(
        f"{with_address if not is_from_me else me} to {with_address if is_from_me else me}: {text if text else extract_text_from_attributed_body(attributed_body) }")

# Close the connection
connection.close()
