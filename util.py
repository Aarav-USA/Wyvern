from typing import Any

import discord

class HoneyCombEmbed(discord.Embed):

    def __init__(self, *args: Any, **kargs: Any) -> None:
        super().__init__(*args, **kargs)
        # gold
        self.colour = 0xFFD700
