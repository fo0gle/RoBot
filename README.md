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

### Step 5: Run the Python Script

Before you want to run it See line 11 and change the number to the number of accounts you have
```sh
python public/ClipboardCopy.py
```

### Step 6: Run the Lua in game
Run the games lua script and for best results clear you clipboard

### Step 7: Wait
just wait

## How to make custom plugins 

### Step 1: Create Plugin Directory
Just make the directory

### Step 2: Create Plugin Files

Inside the plugins directory, create the following files:

* plugin.html
* plugin.css
* plugin.js
* myplugin.dat

They can be named anything just make the dat file the same name as the folder family

### Step 3: Sort out the dat file
```sh
My Plugin
plugin.html
```
At the top is the name you would like your plugin to be called then the bottom is your plugins main html file

### Step 4: Create files

Create the files you would like to do but below is just a simple page

Html:

```sh
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Plugin</title>
    <link rel="stylesheet" href="plugin.css">
    <script src="plugin.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Plugin</h1>
        <p>This is a custom plugin page.</p>
        <button id="alertButton">Click Me</button>
    </div>
</body>
</html>
```

Css:
```sh
.container {
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 5px;
}

h1 {
    color: #333;
}

button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

JavaScript:
```sh
document.addEventListener('DOMContentLoaded', function() {
    const alertButton = document.getElementById('alertButton');
    alertButton.addEventListener('click', function() {
        alert('Button clicked!');
    });
});
```

### Step 5: Install the plugin
Install the plugin by putting it in the plugin folder in public 

### Step 6: Start up the server to see if it works



### Thanks for using this tool 

For anyone who wants to know how the data gets through I am having to use the clipbord, the way it works in the scripts will send the data randomly from 1 to 10 seconds (can be changed) then the python script checks every second for json data on the clipboard. If anyone needs help please put it as I issue then I will help. If anyone wants to help out but some commits in :)
