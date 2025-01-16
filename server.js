const express = require('express');
const WebSocket = require('ws');
const bodyParser = require('body-parser');

// Create an Express app
const app = express();
const port = 3000;

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Use body-parser middleware to parse JSON request bodies
app.use(bodyParser.json());

// Start the HTTP server
const server = app.listen(port, () => {
    console.log(`Server is listening on http://localhost:${port}`);
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

    // Send initial data
    ws.send(JSON.stringify(accounts));
});

// Handle HTTP POST requests to update account data
app.post('/update-accounts', (req, res) => {
    accounts = req.body;
    console.log('Received accounts:', accounts);

    // Broadcast the updated data to all connected WebSocket clients
    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(accounts));
        }
    });

    res.sendStatus(200);
});