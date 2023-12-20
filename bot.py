# bot.py
import aiosqlite
import discord
import os
import responses
from discord.ui import Select, View
from discord.ext import commands
from cogs.Member import Member

class ConfirmView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_confirm = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="Yes", emoji="🏐", description="Yes"),
            discord.SelectOption(label="No", emoji="🏐", description="No")
        ]
    )
    async def select_confirm(self, interaction, select_confirm):
        self.selected_confirm = select_confirm.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_confirm)

async def my_callback(selected_positions):
    print(f"Selected positions: {selected_positions}")

class CustomClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())

    async def on_ready(self):
        self.db = await aiosqlite.connect('Main.db')
        self.cursor = await self.db.cursor()
        await self.cursor.execute("""
                            create table if not exists member (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            author_id VARCHAR(255) NOT NULL,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NOT NULL,
                            nickname VARCHAR(255) NOT NULL,
                            location VARCHAR(255),
                            preferred_location VARCHAR(255),
                            gender VARCHAR(255),
                            pronounce VARCHAR(255),
                            year_of_playing_vb INT,
                            confident_position VARCHAR(255),
                            formation VARCHAR(255),
                            other VARCHAR(255),
                            register VARCHAR(255),
                            purpose VARCHAR(255),
                            email VARCHAR(255),
                            venmo VARCHAR(255),
                            prev_register VARCHAR(255)
                            );"""
        )

        await self.db.commit()

        print(f"{self.user} is now running!")

    async def on_member_join(self, member):

        view_confirm = ConfirmView(callback=my_callback)
        await member.send("歡迎加入！為了方便大家認識你，我們需要你的一些基本資料。\n您是否要開始填寫問卷？", view=view_confirm)
        await view_confirm.wait()
        if view_confirm.selected_confirm[0].lower() == 'no':
            welcome_message = "沒關係！你隨時可以給我下指令 `.新增成員` 來填寫問卷！或是 `.help` 看更多！"
            await member.send(welcome_message)
        elif view_confirm.selected_confirm[0].lower() == 'yes':
            member_cog = Member(self)
            await member_cog.createFirstProfile(member)
        # welcome_message = "歡迎加入！為了方便大家認識你，我們需要你的一些基本資料。\n您是否要開始填寫問卷？"
        # await member.send(welcome_message)

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded Cog: {filename[:-3]}")
            else:
                print("Unable to load pycache folder.")
    
    async def send_message(self, message, user_message, is_private):
        response = responses.handle_response(user_message)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
        else:
            return None

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        
        user_message = str(message.content)
        print("user_message",user_message)
        await self.send_message(message, user_message, is_private=False)

        await super().on_message(message)