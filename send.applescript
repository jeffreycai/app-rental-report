set currentPath to path to me
tell application "System Events"
    set parentFolder to container of currentPath
    set messageFilePath to POSIX path of parentFolder & "/message.txt"
    set fileReference to POSIX file messageFilePath as alias
    set myMessage to read fileReference
end tell

tell application "Messages"
    set myService to 1st service whose service type = iMessage
    set myBuddy to buddy "jeffreycaizhenyuan@gmail.com" of myService
    send myMessage to myBuddy
end tell
