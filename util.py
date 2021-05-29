from typing import Any

import discord

class HoneyCombEmbed(discord.Embed):

    def __init__(self, *args: Any, **kargs: Any) -> None:
        super().__init__(*args, **kargs)
        # gold
        self.colour = 0xFFD700
        
       #Prefix Anouncer
@client.event
async def on_message(message):
    if message.content.startswith = ('<@830310620054290473>'):
        channel = message.channel
        await channel.send('Robot Prefix: hc!')
