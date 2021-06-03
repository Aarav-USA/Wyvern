#YouTube Video Announcer
import discord
import requests

client = discord.Client()

key = "YOUR_API_KEY"
channelId = "UCcvYJZSAk1l5AIT3RG9Y6FA"



@client.event
async def on_message(message):

    if str(message.author) == "Midas' Touch#6946" and message.content.startswith("$midastouch"):
        r = requests.get(
            'https://www.googleapis.com/youtube/v3/search?key=' + key + '&channelId=' + channelId + '&part=snippet,id&order=date&maxResults=1')
        json_data = r.json()
        videoId = json_data["items"][0]["id"]["videoId"]
        await message.channel.purge(limit=1)
        await message.channel.send("Hey @everyone, go check out Midas Touch's latest video!\n"
                                  + "https://youtu.be/" + videoId)
        print(videoId)




client.run('YOUR_TOKEN')

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
