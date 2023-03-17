from applescript import AppleScript
import os

send_imessage_applescript = AppleScript(f'''
    on run argv
        set phoneNumber to item 1 of argv
        set messageText to item 2 of argv

        tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy phoneNumber of targetService
            send messageText to targetBuddy
        end tell
    end run
    ''')


def send_message(recipient_address, message):
    print("sending message to", recipient_address, ": ", message)
    send_imessage_applescript.run(recipient_address, message)


def send_message_to_user(message: str):
    send_message(os.environ["USER_ADDRESS"], message)
