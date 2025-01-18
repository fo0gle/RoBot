const express = require('express');
const WebSocket = require('ws');
const bodyParser = require('body-parser');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;

// Add root redirect before other routes
app.get('/', (req, res) => {
    res.redirect('/home.html');
});

// Define the plugins directory
const PLUGINS_DIRECTORY = path.join(__dirname, 'public', 'plugins');

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Use body-parser middleware to parse JSON request bodies
app.use(bodyParser.json());

// Ensure the plugins directory exists
if (!fs.existsSync(PLUGINS_DIRECTORY)) {
    fs.mkdirSync(PLUGINS_DIRECTORY, { recursive: true });
}

// Route to list plugins
app.get('/plugins', (req, res) => {
    try {
        const plugins = [];
        fs.readdirSync(PLUGINS_DIRECTORY).forEach(pluginName => {
            const pluginPath = path.join(PLUGINS_DIRECTORY, pluginName);
            if (fs.lstatSync(pluginPath).isDirectory()) {
                let mainHtmlFile = null;
                const datFilePath = path.join(pluginPath, `${pluginName}.dat`);
                if (fs.existsSync(datFilePath)) {
                    const lines = fs.readFileSync(datFilePath, 'utf-8').split('\n');
                    if (lines.length >= 2) {
                        mainHtmlFile = lines[1].trim();
                    }
                }
                plugins.push({
                    name: pluginName,
                    main_html_file: mainHtmlFile
                });
            }
        });
        res.json(plugins);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
const server = app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Set up WebSocket server
const wss = new WebSocket.Server({ server });

let accounts = [];

// Handle WebSocket connections
wss.on('connection', (ws) => {
    console.log('Client connected');

    ws.on('close', () => {
        console.log('Client disconnected');
    });

    ws.on('message', (message) => {
        const data = JSON.parse(message);
        accounts.push(data);
        console.log('Received data:', data);

        // Broadcast the data to all connected clients
        wss.clients.forEach(client => {
            if (client.readyState === WebSocket.OPEN) {
                client.send(JSON.stringify(accounts));
            }
        });
    });

    // Send initial data
    ws.send(JSON.stringify(accounts));
});