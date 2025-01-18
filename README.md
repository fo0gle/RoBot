# RoBot

You might ask, what is RoBot? It is a project of mine, an account management platform.

> I do not condone anything that breaks the Roblox Terms of Service.

## What is it

As said earlier, it is an open-source Roblox account management platform which allows you to manage your accounts on other devices.

## Features

- Roblox account tracker
- Remote desktop viewer (It uses RustDesk)
- Custom tracking lua script (used for getting values in games)
- Plugin system
- Settings
- More to come

## Prerequisites

1. **Node.js**: Ensure you have Node.js installed. You can download it from [nodejs.org](https://nodejs.org/).
2. **Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
3. **Git**: Ensure you have Git installed. You can download it from [git-scm.com](https://git-scm.com/).

## Installation

### Step 1: Clone the Repository
Clone your project repository to your local machine.
```sh
git clone <https://github.com/fo0gle/RoBot.git>
cd RobloxBotSite
```

### Step 2: Install Node.js Dependencies
```sh
npm install
```

### Step 3: Install Python Dependencies
```sh
pip install pyperclip websocket-client requests
```

### Step 4: Set Up and Run the Node.js Server
```sh
node server.js
```

The server will be running at http://localhost:3000

### Step 5: Run the Python Scripts
```sh
python public/ClipboardCopy.py
```

### Step 6: Run the Lua in game
Run the games lua script and for best results clear you clipboard

