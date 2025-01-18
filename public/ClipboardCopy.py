import json
import pyperclip
from collections import deque
import websocket

# Dictionary to store the previous state of each account
previous_state = {}

# Change the number of recent clipboards to store (amount of accounts to track)
recent_clipboards = deque(maxlen=10)

def on_open(ws):
    while True:
        clipboard_content = pyperclip.paste()  # Get the most recent thing on the clipboard
        if clipboard_content not in recent_clipboards:
            recent_clipboards.append(clipboard_content)
            try:
                data = json.loads(clipboard_content)  # Attempt to parse the clipboard content as JSON
                if isinstance(data, list):  # Ensure the data is a list
                    for account in data:
                        account_name = account["accountName"]
                        rank = int(account["rank"])
                        gems = int(account["gems"])
                        status = account["status"]
                        playing = account["playing"]

                        # Check if the account has changed
                        if (account_name not in previous_state or 
                            previous_state[account_name]["rank"] != rank or 
                            previous_state[account_name]["gems"] != gems or 
                            previous_state[account_name]["status"] != status or 
                            previous_state[account_name]["playing"] != playing):
                            
                            ws.send(json.dumps(account))
                            previous_state[account_name] = {
                                "rank": rank, 
                                "gems": gems, 
                                "status": status, 
                                "playing": playing
                            }
                            print(f"Updated account: {account_name}")
                            print(f"Sent JSON: {json.dumps(account)}")
            except json.JSONDecodeError:
                print("Clipboard content is not valid JSON")

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("WebSocket closed")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:3000",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()