local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")
local LocalPlayer = Players.LocalPlayer

while true do
    local level = LocalPlayer.leaderstats.Level.value
    local money = LocalPlayer.leaderstats["C$"].value
    local playerName = LocalPlayer.Name
    
    
    local data = {
        {
            accountName = playerName,
            playing = "Fisch",
            level = level,
            money = money,
            status = "Online",
        }
    }
    
    
    local jsonData = HttpService:JSONEncode(data)
    
    
    setclipboard(jsonData)
    print("Data has been copied to the clipboard.")

    local waitTime = math.random(1, 10)  -- Random wait time between 1 and 10 seconds
    wait(waitTime)
end