local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")
local LocalPlayer = Players.LocalPlayer

while true do
    local level = LocalPlayer.Data.Level.Value
    local money = LocalPlayer.Data.Beli.Value
    local playerName = LocalPlayer.Name

    local data = {
        {
            accountName = playerName,
            playing = "BloxFruits",
            level = level,
            money = money,
            status = "Online",
        }
    }

    local jsonData = HttpService:JSONEncode(data)

    setclipboard(jsonData)
    print("Data has been copied to the clipboard.")

    wait(10)  
end