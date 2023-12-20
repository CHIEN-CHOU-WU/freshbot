import discord
import asyncio
from discord.ext import commands
from discord.ui import Select, View
from utils.excel import update_excel

class YearQuaterView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_year_quarter = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="2024 Q1 (Jan - Mar)", emoji="🏐", description="2024 Q1 (Jan - Mar)"),
        ]
    )
    async def select_year_quarter(self, interaction, select_year_quarter):
        self.selected_year_quarter = select_year_quarter.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_year_quarter)

class DatesView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_dates = None

    @discord.ui.select(
        min_values=1,
        max_values=12,
        options = [
            discord.SelectOption(label="1/7", emoji="🏐", description="1/7"),
            discord.SelectOption(label="1/14", emoji="🏐", description="1/14"),
            discord.SelectOption(label="1/21", emoji="🏐", description="1/21"),
            discord.SelectOption(label="1/28", emoji="🏐", description="1/28"),
            discord.SelectOption(label="2/4", emoji="🏐", description="2/4"),
            discord.SelectOption(label="2/11", emoji="🏐", description="2/11"),
            discord.SelectOption(label="2/18", emoji="🏐", description="2/18"),
            discord.SelectOption(label="3/3", emoji="🏐", description="3/3"),
            discord.SelectOption(label="3/10", emoji="🏐", description="3/10"),
            discord.SelectOption(label="3/17", emoji="🏐", description="3/17"),
            discord.SelectOption(label="3/24", emoji="🏐", description="3/24"),
            discord.SelectOption(label="3/31", emoji="🏐", description="3/31"),
        ]
    )

    async def select_dates(self, interaction, select_dates):
        self.selected_dates = select_dates.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_dates)

class YesNoView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_yes_no = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="Yes", emoji="🏐", description="Yes"),
            discord.SelectOption(label="No", emoji="🏐", description="No"),
        ]
    )
    async def select_yes_no(self, interaction, select_yes_no):
        self.selected_yes_no = select_yes_no.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_yes_no)

async def my_callback(selected):
    pass
    # print(f"報名: {selected}")
    

# 報名系統
class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def register_question(self, message):
        try:
            # Year Quarter
            view_year_quarter = YearQuaterView(callback=my_callback)
            await message.channel.send("您想要報名的季度是？", view=view_year_quarter)
            await view_year_quarter.wait()

            if view_year_quarter.selected_year_quarter[0] == "2024 Q1 (Jan - Mar)":
                select_query = """
                select first_name, last_name, nickname
                from member
                where author_id=""" + '"'+str(message.author)+'";'

                self.cursor = await self.bot.db.cursor()
                await self.cursor.execute(select_query)
                result = await self.cursor.fetchone()
                result = list(result)

                if result is None:
                    await message.channel.send(f'我還不認識您誒！請使用 `.新增成員` 加入資料庫喔！或是使用 `.help` 看更多！')
                    return
                
                # Q1
                view_dates = DatesView(callback=my_callback)
                await message.channel.send("可承諾日期(複選)?", view=view_dates)
                await view_dates.wait()

                # Q2
                q2_yn = YesNoView(callback=my_callback)
                await message.channel.send("你可以接受一次練球價格會落在$18-$22之間嗎？（收取費用完全用於場地租金以及器具購買）", view=q2_yn)
                await q2_yn.wait()

                # Q3
                q3_yn = YesNoView(callback=my_callback)
                await message.channel.send("你願意在這季練球前將費用一次付清嗎？", view=q3_yn)
                await q3_yn.wait()

                # Q4
                q4_yn = YesNoView(callback=my_callback)
                await message.channel.send("你有特別想學的嗎？（可跳過）", view=q4_yn)
                await q4_yn.wait()

                result.append(str(view_dates.selected_dates))
                result.append(q2_yn.selected_yes_no[0])
                result.append(q3_yn.selected_yes_no[0])
                result.append(q4_yn.selected_yes_no[0])
                
                if q4_yn.selected_yes_no[0] == "Yes":
                    await message.channel.send('您想要學什麼？')
                    option = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)
                    result.append(option.content)
                else:
                    result.append("")


                return result


        except asyncio.TimeoutError:
            await message.channel.send('您想太久啦~請再使用 `.新增成員` 進行註冊。')
        
    @commands.command(name="報名")
    async def register(self, message):
        
        result = await self.register_question(message)

        if result:
            insert_query = """
            insert into register_2024_Q1 (author_id, first_name, last_name, nickname, dates, price_will_flag, budget_flag, learn_flag, learn_other)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            
            self.cursor = await self.bot.db.cursor()
            await self.cursor.execute(insert_query, (str(message.author), result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
            await self.bot.db.commit()
            await message.channel.send("謝謝你的報名！溫馨提醒，此問卷不代表報名成功。台妹稍過幾日會再公佈報名成功的名字以及收取價錢。請一定要持續鎖定discord社群並開啟email通知。若想學習如何開啟email通知，請至公告專區 -> 好孩子要看頻道 裡查詢開啟email通知。")


async def setup(bot):
    await bot.add_cog(Register(bot))
