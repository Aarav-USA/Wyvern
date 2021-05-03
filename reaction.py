import discord
import json
from discord.ext import commands


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

@client.command()
async def reactrole(ctx, emoji, role: discord.Role,*,message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name':role.name,
            'role_id':role.id,
            'emoji': emoji,
            'message_id':msg.id
        }

        data.append(new_react_role)


    with open('reactrole.json','w') as j:
        json.dump(data,j, indent= 4)

client.run("ODMwMzEwNjIwMDU0MjkwNDcz.YHE1Bg.2Q-1Rnz6pfbvJkyCcQigAuBeiCY")