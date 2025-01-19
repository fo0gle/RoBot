# THIS IS FOR TESTING PURPOSES ONLY IT IS NOT USEFUL




import requests
import json

url = "http://localhost:3000/update-accounts"

# List of Roblox user IDs
user_ids = [
    "",
    "1234567890",
    # Add more user IDs as needed
]

# Function to get profile data using Roblox API
def get_profile_data(user_id):
    # API endpoint to get user information
    user_info_url = f"https://users.roblox.com/v1/users/{user_id}"
    presence_url = f"https://presence.roblox.com/v1/presence/users"
    
    # Get user information
    user_info_response = requests.get(user_info_url)
    user_info = user_info_response.json()
    
    # Get user presence (online status)
    presence_response = requests.post(presence_url, json={"userIds": [user_id]})
    presence_info = presence_response.json()
    
    # Extract account display name
    display_name = user_info.get('displayName', 'Name not found')
    
    # Extract status
    presence_data = presence_info['userPresences'][0]
    status = presence_data.get('userPresenceType', 'Status not found')
    status_map = {0: 'Offline', 1: 'Online', 2: 'In Game', 3: 'In Studio'}
    status_text = status_map.get(status, 'Unknown')
    
    return {
        "name": display_name,
        "status": status_text
    }

# List to store profile data
profiles = []

for user_id in user_ids:
    profile_data = get_profile_data(user_id)
    profiles.append(profile_data)

# Example data
accounts = profiles

# Send data to the server
response = requests.post(url, json=accounts)
print(f"Response status code: {response.status_code}")
print(f"Response text: {response.text}")

# Print the profile data
for profile in profiles:
    print(f"Name: {profile['name']}, Status: {profile['status']}")