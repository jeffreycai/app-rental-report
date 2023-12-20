import subprocess
import os
import datetime

# Function to execute compiled AppleScript
def send_imessage():
    script_path = os.path.join(os.path.dirname(__file__), 'send.scpt')
    subprocess.run(["osascript", script_path])

# Function to check if the script was run in the last 48 hours
def last_run_within_48_hours(log_file):
    if not os.path.exists(log_file):
        return False
    
    with open(log_file, 'r') as file:
        for line in reversed(file.readlines()):
            if 'success' in line:
                try:
                    last_run_time = datetime.datetime.strptime(line.split(',')[0], '%Y-%m-%d %H:%M:%S')
                    return (datetime.datetime.now() - last_run_time) < datetime.timedelta(hours=48)
                except ValueError:
                    # Handle cases where the line does not have a valid timestamp
                    continue
    
    return False

# Logging function
def log_run(message, log_file):
    with open(log_file, 'a') as file:
        file.write(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S}, {message}\n')

# Main script logic
log_file = 'run_log.txt'

if last_run_within_48_hours(log_file):
    log_run('Message already sent in last 48 hours, skip', log_file)
    print('Message already sent in last 48 hours, skip')
else:
    send_imessage()
    log_run(f'Message sent successfully to {os.getenv("TARGET")}', log_file)
