import json
import time
import websocket
import pyperclip

# WebSocket server URL
ws_url = "ws://localhost:3000"

# Dictionary to store the previous state of each account
previous_state = {}

def on_open(ws):
    while True:
        clipboard_content = pyperclip.paste()  # Get the most recent thing on the clipboard
        try:
            data = json.loads(clipboard_content)  # Attempt to parse the clipboard content as JSON
            if isinstance(data, list):  # Ensure the data is a list
                for account in data:
                    account_name = account["accountName"]
                    level = account["level"]
                    money = account["money"]

                    # Check if the account has changed
                    if account_name not in previous_state or previous_state[account_name]["level"] != level or previous_state[account_name]["money"] != money:
                        ws.send(json.dumps(account))
                        pyperclip.copy(str(level))  # Copy the level to the clipboard
                        previous_state[account_name] = {"level": level, "money": money}
                        print(f"Updated account: {account_name}")
                    else:
                        print(f"No changes for account: {account_name}")
            else:
                print("Clipboard content is not a list.")
        except json.JSONDecodeError:
            print("Clipboard content is not valid JSON.")
        
        time.sleep(1)  # Wait for 1 second before repeating

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()