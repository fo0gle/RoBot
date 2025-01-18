local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")
local LocalPlayer = Players.LocalPlayer

while true do
    local rank = LocalPlayer.leaderstats["⭐ Rank"].Value
    local gems = LocalPlayer.leaderstats["💎 Diamonds"].Value
    local playerName = LocalPlayer.Name

    local data = {
        accountName = playerName,
        playing = "PetSim99",
        rank = rank,
        gems = gems,
        status = "Online",
    }

    local jsonData = HttpService:JSONEncode({data})

    setclipboard(jsonData)
    print("Data has been copied to the clipboard.")

    local waitTime = math.random(1, 10)  -- Random wait time between 1 and 10 seconds
    wait(waitTime)
end