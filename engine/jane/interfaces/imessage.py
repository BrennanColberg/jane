from applescript import AppleScript

applescript_code = f'''
on run argv
    set phoneNumber to item 1 of argv
    set messageText to item 2 of argv

    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy phoneNumber of targetService
        send messageText to targetBuddy
    end tell
end run
'''

applescript = AppleScript(applescript_code)
applescript.run('', 'test message')
