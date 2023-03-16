# this is very complicated as an interface, do later
# (probably with separate server, once there's an API)

from applescript import AppleScript


def send(address: str, message: str):
    AppleScript(f'''
        on run argv
            set phoneNumber to item 1 of argv
            set messageText to item 2 of argv

            tell application "Messages"
                set targetService to 1st service whose service type = iMessage
                set targetBuddy to buddy phoneNumber of targetService
                send messageText to targetBuddy
            end tell
        end run
    ''').run(address, message)
