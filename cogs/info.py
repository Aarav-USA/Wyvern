from discord.ext import commands

import util

# HoneyComb bot information commands.
class Info(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.config = getattr(bot, 'config')

    @commands.command(help='Link source code')
    async def source(self, ctx: commands.Context) -> None:
        embed = util.HoneyCombEmbed(
            title='Check out my source code!',
            url=self.config['DEFAULT']['SourceURL']
        )
        await ctx.send(embed=embed)

    @commands.command(help='Link support server', aliases=['su'])
    async def support(self, ctx: commands.Context) -> None:
        await ctx.send(self.config['DEFAULT']['SupportServer'])

def setup(bot: commands.Bot) -> None:
    print('Loading info extension...')
    bot.add_cog(Info(bot))
