import json
import pyperclip
from collections import deque
import websocket
import re

# Dictionary to store the previous state of each account
previous_state = {}

# Change the number of recent clipboards to store (amount of accounts to track)
recent_clipboards = deque(maxlen=10)

def clean_number(value):
    """Remove non-numeric characters from a string."""
    return int(re.sub(r'\D', '', str(value)))

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
                        playing = account["playing"]
                        status = account["status"]

                        # Handle different game-specific fields
                        if playing == "PetSim99":
                            rank = clean_number(account["rank"])
                            gems = clean_number(account["gems"])
                            game_specific_data = {
                                "rank": rank,
                                "gems": gems
                            }
                        elif playing == "Fisch":
                            level = clean_number(account["level"])
                            money = clean_number(account["money"])
                            game_specific_data = {
                                "level": level,
                                "money": money
                            }
                        elif playing == "BloxFruits":
                            level = clean_number(account["level"])
                            money = clean_number(account["money"])
                            game_specific_data = {
                                "level": level,
                                "money": money
                            }
                        else:
                            game_specific_data = {}

                        # Check if the account has changed
                        if (account_name not in previous_state or 
                            previous_state[account_name].get("rank") != game_specific_data.get("rank") or 
                            previous_state[account_name].get("gems") != game_specific_data.get("gems") or 
                            previous_state[account_name].get("level") != game_specific_data.get("level") or 
                            previous_state[account_name].get("money") != game_specific_data.get("money") or 
                            previous_state[account_name]["status"] != status or 
                            previous_state[account_name]["playing"] != playing):
                            
                            ws.send(json.dumps(account))
                            previous_state[account_name] = {
                                "playing": playing,
                                "status": status,
                                **game_specific_data
                            }
                            print(f"Updated account: {account_name}")
                            print(f"Sent JSON: {json.dumps(account)}")
            except json.JSONDecodeError:
                print("Clipboard content is not valid JSON")

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:3000",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()