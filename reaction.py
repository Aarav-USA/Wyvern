import discord
import json
from discord.ext import commands

JSON_FILE = 'reactions.json'

class ReactRole(commands.Cog):

    def __init__(self, bot: commands.Bot, json_file: str) -> None:
        self.bot = bot
        self.json_file = json_file

    # Saves a react role to the JSON file; does not catch exceptions.
    def __save_role_record(self, emoji: str, role: discord.Role,
            msg: discord.Message) -> None:
        role_record = {
            'role_name' : role.name,
            'role_id' : role.id,
            'emoji' : emoji,
            'message_id' : msg.id
        }

        with open(self.json_file, 'w') as file_handle:
            react_roles = json.load(file_handle)
        react_roles.append(role_record)

        with open(self.json_file, 'r') as file_handle:
            json.dump(react_roles, file_handle, indent=4)
            
    @commands.command()
    async def reactrole(self, ctx: commands.Context, emoji: str,
            role: discord.Role, *, message: str):
        emb = discord.Embed(description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emoji)
        self.__save_role_record(emoji, role, msg)

client = commands.Bot(command_prefix="hc!",intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now online")
    print("----------------------------------------------")

@client.event
async def on_raw_reaction_add(payload):


        with open('reactrole.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

client.add_cog(ReactRole(client, JSON_FILE))

if __name__ == '__main__':
    client.run("ODMwMzEwNjIwMDU0MjkwNDcz.YHE1Bg.2Q-1Rnz6pfbvJkyCcQigAuBeiCY")

def setup(bot: commands.Bot):
    print('Loading reactrole extension...')
    return ReactRole(bot, JSON_FILE)
