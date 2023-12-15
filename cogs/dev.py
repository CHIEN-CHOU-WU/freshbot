import discord
from utils.excel import update_excel
from discord.ext import commands
from discord import app_commands

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reload")
    async def reload(self, ctx, extension):
        await self.bot.unload_extension(f'cogs.{extension}')
        await self.bot.load_extension(f'cogs.{extension}')
        await ctx.send('Done!')

    @commands.command(name="excel")
    async def excel(self,ctx):
        await update_excel(ctx, message_flag=True)

async def setup(bot):
    await bot.add_cog(Dev(bot))