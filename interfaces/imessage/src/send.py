from applescript import AppleScript
import sqlite3

connection = sqlite3.connect('~/Library/Messages/chat.db')

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


def send_imessage(recipient_address, message):
    """send iMessage"""
    send_imessage_applescript.run(recipient_address, message)
