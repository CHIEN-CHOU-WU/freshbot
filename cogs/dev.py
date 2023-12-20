import discord
from utils.excel import update_excel
from utils.database import delete_data
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

    @commands.command(name="del")
    async def delete(self,ctx, first_name, last_name, nickname):
        await delete_data(first_name, last_name, nickname)
        await ctx.send('Done!')


async def setup(bot):
    await bot.add_cog(Dev(bot))