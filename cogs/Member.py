import discord
import asyncio
from discord.ext import commands
from discord.ui import Select, View
from utils.excel import update_excel

class PositionView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_position = None

    @discord.ui.select(
        min_values=1,
        max_values=5,
        options = [
            discord.SelectOption(label="大砲 (Outside Hitter)", emoji="🏐", description="大砲 (Outside Hitter)"),
            discord.SelectOption(label="自由 (Libero)", emoji="🏐", description="自由 (Libero)"),
            discord.SelectOption(label="舉球 (Setter)", emoji="🏐", description="舉球 (Setter)"),
            discord.SelectOption(label="欄中 (Middle Blocker)", emoji="🏐", description="欄中 (Middle Blocker)"),
            discord.SelectOption(label="輔舉/副位 (Opposite Hitter)", emoji="🏐", description="輔舉/副位 (Opposite Hitter)")
        ]
    )
    async def select_position(self, interaction, select_position):
        self.selected_position = select_position.values
        res = "哇嗚～我也喜歡打 "
        for value in select_position.values:
            res += value + ','
        res = res[:-1] + '!'
        await interaction.message.edit(view=self)
        await interaction.response.send_message(res)
        # await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_position)
class LocationView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_location = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="Manhattan", emoji="🏐", description="Manhattan"),
            discord.SelectOption(label="Brooklyn", emoji="🏐", description="Brooklyn"),
            discord.SelectOption(label="Bronx", emoji="🏐", description="Bronx"),
            discord.SelectOption(label="Queens", emoji="🏐", description="Queens"),
            discord.SelectOption(label="New Jersey", emoji="🏐", description="New Jersey"),
            discord.SelectOption(label="Other", emoji="🏐", description="Other"),
        ]
    )
    async def select_location(self, interaction, select_location):
        self.selected_location = select_location.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_location)
class PreferredLocationView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_preferred_location = None

    @discord.ui.select(
        min_values=1,
        max_values=6,
        options = [
            discord.SelectOption(label="Manhattan", emoji="🏐", description="Manhattan"),
            discord.SelectOption(label="Brooklyn", emoji="🏐", description="Brooklyn"),
            discord.SelectOption(label="Bronx", emoji="🏐", description="Bronx"),
            discord.SelectOption(label="Queens", emoji="🏐", description="Queens"),
            discord.SelectOption(label="New Jersey", emoji="🏐", description="New Jersey"),
            discord.SelectOption(label="Any", emoji="🏐", description="Any"),
        ]
    )
    async def select_preferred_location(self, interaction, select_preferred_location):
        self.selected_preferred_location = select_preferred_location.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_preferred_location)
class GenderView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_gender = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="F", emoji="🏐", description="F"),
            discord.SelectOption(label="M", emoji="🏐", description="M"),
            discord.SelectOption(label="Other", emoji="🏐", description="Other"),
            discord.SelectOption(label="Prefer not to answer", emoji="🏐", description="Prefer not to answer"),
        ]
    )
    async def select_gender(self, interaction, select_gender):
        self.selected_gender = select_gender.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_gender)
class PronounceView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_pronounce = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="She/her", emoji="🏐", description="She/her"),
            discord.SelectOption(label="He/Him", emoji="🏐", description="He/Him"),
            discord.SelectOption(label="They/them", emoji="🏐", description="They/them"),
        ]
    )
    async def select_pronounce(self, interaction, select_pronounce):
        self.selected_pronounce = select_pronounce.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_pronounce)
class FormationView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_formation = None

    @discord.ui.select(
        min_values=1,
        max_values=5,
        options = [
            discord.SelectOption(label="無", emoji="🏐", description="無"),
            discord.SelectOption(label="輪轉舉球", emoji="🏐", description="輪轉舉球"),
            discord.SelectOption(label="單舉 (5-1)", emoji="🏐", description="單舉 (5-1)"),
            discord.SelectOption(label="前排雙舉 (4-2)", emoji="🏐", description="前排雙舉 (4-2)"),
            discord.SelectOption(label="後排雙舉 (6-2)", emoji="🏐", description="後排雙舉 (6-2)"),
        ]
    )
    async def select_formation(self, interaction, select_formation):
        self.selected_formation = select_formation.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_formation)
class OtherView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_other = None

    @discord.ui.select(
        min_values=1,
        max_values=5,
        options = [
            discord.SelectOption(label="無", emoji="🏐", description="無"),
            discord.SelectOption(label="校隊", emoji="🏐", description="校隊"),
            discord.SelectOption(label="系隊", emoji="🏐", description="系隊"),
            discord.SelectOption(label="Club Team", emoji="🏐", description="Club Team"),
            discord.SelectOption(label="Open Play", emoji="🏐", description="Open Play"),
            discord.SelectOption(label="Other", emoji="🏐", description="Other"),
        ]
    )
    async def select_other(self, interaction, select_other):
        self.selected_other = select_other.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_other)
class RegisterView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_register = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="Yes", emoji="🏐", description="Yes"),
            discord.SelectOption(label="No", emoji="🏐", description="No")
        ]
    )
    async def select_register(self, interaction, select_register):
        self.selected_register = select_register.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_register)
class PreviousRegisterView(View):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.selected_prev_register = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="Yes", emoji="🏐", description="Yes"),
            discord.SelectOption(label="No", emoji="🏐", description="No")
        ]
    )
    async def select_prev_register(self, interaction, select_prev_register):
        self.selected_prev_register = select_prev_register.values
        await interaction.response.defer()
        self.stop()

        if self.callback:
            await self.callback(self.selected_prev_register)
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

class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def set_permissions(self, message, channel_id, read_messages=True, send_messages=True, view_channel=True, add_reactions=True, manage_messages=True, manage_threads=True, read_message_history=True, create_public_threads=True, send_messages_in_threads=True):
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.set_permissions(message.author,
                                  read_messages=read_messages,
                                  send_messages=send_messages,
                                  view_channel=view_channel,
                                  add_reactions=add_reactions,  
                                  manage_messages=manage_messages,
                                  read_message_history=read_message_history,
                                  manage_threads=manage_threads,
                                  create_public_threads = create_public_threads,
                                  send_messages_in_threads = send_messages_in_threads
                                  )

    async def getPii(self, message):
        try:
            # first name
            await message.channel.send('您的名字是? (1/15)')
            first_name = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)

            # last name
            await message.channel.send('您的姓氏是? (2/15)')
            last_name = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)

            # nickname
            await message.channel.send('您的小名是? (3/15)')
            nickname = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)


            return first_name.content, last_name.content, nickname.content
        except asyncio.TimeoutError:
            await message.channel.send('您想太久啦~請再使用 `.新增成員` 進行註冊。')
    
    async def getPii2(self, message):
        try:

            # location
            view_location = LocationView(callback=my_callback)
            await message.channel.send("您的居住地區? (4/15)", view=view_location)
            await view_location.wait()

            if view_location.selected_location[0] == "Other":
                await message.channel.send('請填寫您的居住地區:')
                view_location.selected_location[0] = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)
                view_location.selected_location[0] = view_location.selected_location[0].content

            # preferred location
            view_preferred_location = PreferredLocationView(callback=my_callback)
            await message.channel.send("您有興趣 open play 的地點?（可複選）(5/15)", view=view_preferred_location)
            await view_preferred_location.wait()

            # Gender
            view_gender = GenderView(callback=my_callback)
            await message.channel.send("您的性別? (6/15)", view=view_gender)
            await view_gender.wait()

            # Pronounce
            view_pronounce = PronounceView(callback=my_callback)
            await message.channel.send('您希望怎麼被稱呼? (7/15)', view=view_pronounce)
            await view_pronounce.wait()

            # year_of_playing_vb
            await message.channel.send('您的排球球齡? (8/15)')
            year_of_playing_vb = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)
            
            # confident position
            view_confident_position = PositionView(callback=my_callback)
            await message.channel.send("您最喜歡/擅長的排球位置?（可複選）(9/15)", view=view_confident_position)
            await view_confident_position.wait()

            # formation
            view_formation = FormationView(callback=my_callback)
            await message.channel.send("曾跑過的隊形?（可複選）(10/15)", view=view_formation)
            await view_formation.wait()

            # other
            view_other = OtherView(callback=my_callback)
            await message.channel.send("其他經歷?（可複選）(11/15)", view=view_other)
            await view_other.wait()

            if "Other" in view_other.selected_other:
                await message.channel.send('請填寫其他:')
                other_answer = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)
                other_answer = other_answer.content
                view_other.selected_other = [other_answer if item == 'Other' else item for item in view_other.selected_other]
            # if view_other.selected_other[0] == "Other":
            #     await message.channel.send('請填寫其他:')
            #     view_other.selected_other[0] = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)
                print("view_other.selected_other",view_other.selected_other)

            return view_location.selected_location[0], view_preferred_location.selected_preferred_location, view_gender.selected_gender[0], view_pronounce.selected_pronounce[0], year_of_playing_vb.content, view_confident_position.selected_position, view_formation.selected_formation, view_other.selected_other

        except asyncio.TimeoutError:
            await message.channel.send('您想太久啦~請再使用 `.新增成員` 進行註冊。')

    async def getRegister(self, message):
        try:
            purpose = None
            email = None
            venmo = None

            # register flag
            view_register = RegisterView(callback=my_callback)
            await message.channel.send("是否有已報名本季 Fresh 練習 2023 Q4? (12/15)", view=view_register)
            await view_register.wait()

            if view_register.selected_register[0] == "Yes":
                # purpose
                await message.channel.send('想加入練球的目的？ (13/15)')
                purpose = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)

                # email
                await message.channel.send('您的 email? (此資料只適用於練習收費以及緊急公告內部使用，我們不會將這項資訊外洩給他人) (14/15)')
                email = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=60.0)

                # venmo
                await message.channel.send('您的 venmo? (此資料只適用於練習收費以及緊急公告內部使用，我們不會將這項資訊外洩給他人) (15/15)')
                venmo = await self.bot.wait_for('message', check=lambda m: m.author == message.author, timeout=600.0)

                # 台妹練球專區/2023
                await self.set_permissions(message, channel_id=1185215519134076928)
                # 台妹練球專區/校友練習生
                await self.set_permissions(message, channel_id=1185220547135672381)

                await message.channel.send('感謝你的參與捏！恭喜您解鎖練球專區 -> 2023 頻道! \n 您可以在當季 Thread 討論練球事宜喔！也歡迎你在open play專區尋找球友，隨便逛逛啊！謝謝！')
                
                return view_register.selected_register[0], purpose.content, email.content, venmo.content, None

            if view_register.selected_register[0] == "No":
                # get previous register flag
                view_prev_register = PreviousRegisterView(callback=my_callback)
                await message.channel.send("雖然現在沒有參與，但是否有參與過任何一季練習? (15/15)", view=view_prev_register)
                await view_prev_register.wait()

                if view_prev_register.selected_prev_register[0] == "Yes":
                    # 台妹練球專區/校友練習生
                    await self.set_permissions(message, channel_id=1185220547135672381)

                    await message.channel.send('感謝你的參與捏！恭喜你解鎖練球專區 ->校友練習生頻道歡迎在這裡跟你的球友say hi！也歡迎你在open play專區尋找球友，隨便逛逛啊！謝謝！')

                elif view_prev_register.selected_prev_register[0] == "No":
                    pass

                    await message.channel.send('希望台妹能夠在未來能為你服務，若想要報名練球， 練球專區 ->報名練習問卷 填寫報名問卷 也歡迎你在open play專區尋找球友，隨便逛逛啊！謝謝！')

                return view_register.selected_register[0], purpose, email, venmo, view_prev_register.selected_prev_register[0]

        except asyncio.TimeoutError:
            await message.channel.send('您想太久啦~請再使用 `.新增成員` 進行註冊。')

    def embedProfile(self, result):
        embed = discord.Embed(title="User Profile", color=0x00ff00)
        embed.add_field(name="姓", value=result[2], inline=True)
        embed.add_field(name="名字", value=result[3], inline=True)
        embed.add_field(name="小名", value=result[4], inline=True)
        embed.add_field(name="性別", value=result[7], inline=True)
        embed.add_field(name="稱呼", value=result[8], inline=True)
        embed.add_field(name="現居", value=result[5], inline=True)
        embed.add_field(name="球齡", value=result[9], inline=True)
        embed.add_field(name="擅長位置", value=result[10], inline=True)
        embed.add_field(name="打過隊形", value=result[11], inline=True)
        embed.add_field(name="其他", value=result[12], inline=True)
        return embed

    def embedAllProfile(self, result):
        embed = discord.Embed(title="User Profile", color=0x00ff00)
        embed.add_field(name="姓", value=result[2], inline=True)
        embed.add_field(name="名字", value=result[3], inline=True)
        embed.add_field(name="小名", value=result[4], inline=True)
        embed.add_field(name="性別", value=result[7], inline=True)
        embed.add_field(name="稱呼", value=result[8], inline=True)
        embed.add_field(name="現居", value=result[5], inline=True)
        embed.add_field(name="希望練球地點", value=result[6], inline=True)
        embed.add_field(name="球齡", value=result[9], inline=True)
        embed.add_field(name="擅長位置", value=result[10], inline=True)
        embed.add_field(name="打過隊形", value=result[11], inline=True)
        embed.add_field(name="其他", value=result[12], inline=True)
        embed.add_field(name="是否已報名本季", value=result[13], inline=True)
        embed.add_field(name="報名目的", value=result[14], inline=True)
        embed.add_field(name="Email", value=result[15], inline=True)
        embed.add_field(name="Venmo", value=result[16], inline=True)
        embed.add_field(name="是否有參與過任何一季", value=result[17], inline=True)
        return embed

    @commands.command(name="新增成員")
    async def createProfile(self, message):
        # find id to according name
        select_query = """
        select id
        from member
        where author_id=""" + '"'+str(message.author)+'";'

        self.cursor = await self.bot.db.cursor()
        await self.cursor.execute(select_query)
        result = await self.cursor.fetchone()

        if result is not None:
            return await message.channel.send(f'您已經在名單裡啦! \n請使用 `.更新成員` 來更新 或是使用 .help 看更多!')
        
        # Pii
        first_name, last_name, nickname = await self.getPii(message)
        
        # Pii 2
        location, preferred_location, gender, pronounce, year_of_playing_vb, confident_position, formation, other = await self.getPii2(message)
        # Fresh Related Questions
        register, purpose, email, venmo, prev_register = await self.getRegister(message)

        insert_query = """
        insert into member (author_id, first_name, last_name, nickname, location, preferred_location, gender, pronounce, year_of_playing_vb, confident_position, formation, other, register, purpose, email, venmo, prev_register)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        await self.cursor.execute(insert_query, (str(message.author), first_name, last_name, nickname, str(location), str(preferred_location), str(gender), str(pronounce), year_of_playing_vb, str(confident_position), str(formation), str(other), str(register), purpose, email, venmo, str(prev_register)))
        await self.bot.db.commit()
        
        # Open Play manhattan, queens,new-jersy, bronx, brooklyn
        await self.set_permissions(message, channel_id=1166533138911076362, send_messages=False)
        await self.set_permissions(message, channel_id=1166543179252760668, send_messages=False)
        await self.set_permissions(message, channel_id=1166543213541216256, send_messages=False)
        await self.set_permissions(message, channel_id=1181709100132872253, send_messages=False)
        await self.set_permissions(message, channel_id=1185084178379837530, send_messages=False)
        # 活動專區/2024波紐馬
        await self.set_permissions(message, channel_id=1185224900630282282)
        # 聊天專區/閒聊
        await self.set_permissions(message, channel_id=1166544890386206812)
        # 聊天專區/排球比賽討論
        await self.set_permissions(message, channel_id=1166544930655711353)
        # 聊天專區/健身
        await self.set_permissions(message, channel_id=1173996775275778058)
        # 聊天專區/復健
        await self.set_permissions(message, channel_id=1173996804258402335)

        # 在 "新成員報到" channel 恭喜
        channel = self.bot.get_channel(1166533087493103668)
        select_query = """
        select
        *
        from member
        where first_name=? and last_name=? and nickname=?;"""

        self.cursor = await self.bot.db.cursor()
        await self.cursor.execute(select_query, (first_name, last_name, nickname))
        result = await self.cursor.fetchone()
        
        embed = self.embedProfile(result)

        await update_excel(channel, message_flag=False)

        await channel.send(f"恭喜 {nickname} 加入！歡迎！", embed=embed)

    @commands.command(name="更新成員")
    async def updateProfile(self, message):
        # find id to according to author_id
        select_query = """
        select *
        from member
        where author_id=""" + '"'+str(message.author)+'";'
        self.cursor = await self.bot.db.cursor()
        await self.cursor.execute(select_query)
        
        result = await self.cursor.fetchone()
        if result is not None:
            embed = self.embedProfile(result)
            await message.channel.send(embed=embed)
            view_confirm = ConfirmView(callback=my_callback)
            await message.channel.send("這是您嗎？", view=view_confirm)
            await view_confirm.wait()
        if view_confirm.selected_confirm[0].lower() == 'no':
            return
        elif view_confirm.selected_confirm[0].lower() == 'yes':
            # Pii 2
            location, preferred_location, gender, pronounce, year_of_playing_vb, confident_position, formation, other = await self.getPii2(message)
            # Fresh Related Questions
            register, purpose, email, venmo, prev_register = await self.getRegister(message)

            update_query = """
            UPDATE member
            SET location = ?, preferred_location = ?, gender = ?, pronounce = ?, year_of_playing_vb = ?, confident_position = ?, formation = ?, other = ?, register = ?, purpose = ?, email = ?, venmo = ?, prev_register = ?
            WHERE author_id=""" + '"'+str(message.author)+'";'
            await self.cursor.execute(update_query, (str(location), str(preferred_location), str(gender), str(pronounce), year_of_playing_vb, str(confident_position), str(formation), str(other), str(register), purpose, email, venmo, str(prev_register)))
            await self.bot.db.commit()
            select_query = """
            select *
            from member
            where author_id=""" + '"'+str(message.author)+'";'

            self.cursor = await self.bot.db.cursor()
            await self.cursor.execute(select_query)
            
            result = await self.cursor.fetchone()
            embed = self.embedAllProfile(result)
            await message.channel.send(embed=embed)
            await message.channel.send(f'您已成功更新! 使用 .help 看更多!')
        
    @commands.command(name="成員")
    async def showProfile(self, message):
        select_query = """
        select
        *
        from member"""

        self.cursor = await self.bot.db.cursor()
        await self.cursor.execute(select_query)
        results = await self.cursor.fetchall()
        
        if results is not None:
            for result in results:
                embed = self.embedProfile(result)
                await message.channel.send(embed=embed)
    
    @commands.command(name="我")
    async def showMyProfile(self, message):
        # find id to according to author_id
        select_query = """
        select *
        from member
        where author_id=""" + '"'+str(message.author)+'";'
        self.cursor = await self.bot.db.cursor()
        await self.cursor.execute(select_query)
        
        result = await self.cursor.fetchone()
        if result is not None:
            embed = self.embedAllProfile(result)
            await message.author.send(embed=embed)


# For member on join
    async def set_permissions_member(self, member, channel_id, read_messages=True, send_messages=True, view_channel=True, add_reactions=True, manage_messages=True, manage_threads=True, read_message_history=True, create_public_threads=True, send_messages_in_threads=True):    
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.set_permissions(member,
                                  read_messages=read_messages,
                                  send_messages=send_messages,
                                  view_channel=view_channel,
                                  add_reactions=add_reactions,  
                                  manage_messages=manage_messages,
                                  read_message_history=read_message_history,
                                  manage_threads=manage_threads,
                                  create_public_threads = create_public_threads,
                                  send_messages_in_threads = send_messages_in_threads
                                  )
    async def getPiiMember(self, member):
        try:
            # first name
            await member.send('您的名字是? (1/15)')
            first_name = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)

            # last name
            await member.send('您的姓氏是? (2/15)')
            last_name = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)

            # nickname
            await member.send('您的小名是? (3/15)')
            nickname = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)


            return first_name.content, last_name.content, nickname.content
        except asyncio.TimeoutError:
            await member.send('您想太久啦~請再使用 `.新增成員` 進行註冊。')
    
    async def getPiiMember2(self, member):
        try:

            # location
            view_location = LocationView(callback=my_callback)
            await member.send("您的居住地區? (4/15)", view=view_location)
            await view_location.wait()

            if view_location.selected_location[0] == "Other":
                await member.send('請填寫您的居住地區:')
                view_location.selected_location[0] = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)
                view_location.selected_location[0] = view_location.selected_location[0].content

            # preferred location
            view_preferred_location = PreferredLocationView(callback=my_callback)
            await member.send("您有興趣 open play 的地點?（可複選）(5/15)", view=view_preferred_location)
            await view_preferred_location.wait()

            # Gender
            view_gender = GenderView(callback=my_callback)
            await member.send("您的性別? (6/15)", view=view_gender)
            await view_gender.wait()

            # Pronounce
            view_pronounce = PronounceView(callback=my_callback)
            await member.send('您希望怎麼被稱呼? (7/15)', view=view_pronounce)
            await view_pronounce.wait()

            # year_of_playing_vb
            await member.send('您的排球球齡? (8/15)')
            year_of_playing_vb = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)
            
            # confident position
            view_confident_position = PositionView(callback=my_callback)
            await member.send("您最喜歡/擅長的排球位置?（可複選）(9/15)", view=view_confident_position)
            await view_confident_position.wait()

            # formation
            view_formation = FormationView(callback=my_callback)
            await member.send("曾跑過的隊形?（可複選）(10/15)", view=view_formation)
            await view_formation.wait()

            # other
            view_other = OtherView(callback=my_callback)
            await member.send("其他經歷?（可複選）(11/15)", view=view_other)
            await view_other.wait()

            if "Other" in view_other.selected_other:
                await member.send('請填寫其他:')
                other_answer = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)
                other_answer = other_answer.content
                view_other.selected_other = [other_answer if item == 'Other' else item for item in view_other.selected_other]

            return view_location.selected_location[0], view_preferred_location.selected_preferred_location, view_gender.selected_gender[0], view_pronounce.selected_pronounce[0], year_of_playing_vb.content, view_confident_position.selected_position, view_formation.selected_formation, view_other.selected_other

        except asyncio.TimeoutError:
            await member.send('您想太久啦~請再使用 `.新增成員` 進行註冊。')

    async def getRegisterMember(self, member):
        try:
            purpose = None
            email = None
            venmo = None

            # register flag
            view_register = RegisterView(callback=my_callback)
            await member.send("是否有已報名本季 Fresh 練習 2023 Q4? (12/15)", view=view_register)
            await view_register.wait()

            if view_register.selected_register[0] == "Yes":
                # purpose
                await member.send('想加入練球的目的？ (13/15)')
                purpose = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)

                # email
                await member.send('您的 email? (此資料只適用於練習收費以及緊急公告內部使用，我們不會將這項資訊外洩給他人) (14/15)')
                email = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=60.0)

                # venmo
                await member.send('您的 venmo? (此資料只適用於練習收費以及緊急公告內部使用，我們不會將這項資訊外洩給他人) (15/15)')
                venmo = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=600.0)

                # 台妹練球專區/2023
                await self.set_permissions_member(member, channel_id=1185215519134076928)
                # 台妹練球專區/校友練習生
                await self.set_permissions_member(member, channel_id=1185220547135672381)

                await member.send('感謝你的參與捏！恭喜您解鎖練球專區 -> 2023 頻道! \n 您可以在當季 Thread 討論練球事宜喔！也歡迎你在open play專區尋找球友，隨便逛逛啊！謝謝！')
                
                return view_register.selected_register[0], purpose.content, email.content, venmo.content, None

            if view_register.selected_register[0] == "No":
                # get previous register flag
                view_prev_register = PreviousRegisterView(callback=my_callback)
                await member.send("雖然現在沒有參與，但是否有參與過任何一季練習? (15/15)", view=view_prev_register)
                await view_prev_register.wait()

                if view_prev_register.selected_prev_register[0] == "Yes":
                    # 台妹練球專區/校友練習生
                    await self.set_permissions_member(member, channel_id=1185220547135672381)

                    await member.send('感謝你的參與捏！恭喜你解鎖練球專區 ->校友練習生頻道歡迎在這裡跟你的球友say hi！也歡迎你在open play專區尋找球友，隨便逛逛啊！謝謝！')

                elif view_prev_register.selected_prev_register[0] == "No":
                    pass

                    await member.send('希望台妹能夠在未來能為你服務，若想要報名練球， 練球專區 ->報名練習問卷 填寫報名問卷 也歡迎你在open play專區尋找球友，隨便逛逛啊！謝謝！')

                return view_register.selected_register[0], purpose, email, venmo, view_prev_register.selected_prev_register[0]

        except asyncio.TimeoutError:
            await member.send('您想太久啦~請再使用 `.新增成員` 進行註冊。')
    
    async def createFirstProfile(self, member):
        # find id to according name
        select_query = """
        select id
        from member
        where author_id=""" + '"'+str(member)+'";'

        self.cursor = await self.bot.db.cursor()
        await self.cursor.execute(select_query)
        result = await self.cursor.fetchone()

        if result is not None:
            return await member.send(f'您已經在名單裡啦! \n請使用 `.更新成員` 來更新 或是使用 .help 看更多!')
        
        # Pii
        first_name, last_name, nickname = await self.getPiiMember(member)
        
        # Pii 2
        location, preferred_location, gender, pronounce, year_of_playing_vb, confident_position, formation, other = await self.getPiiMember2(member)
        # Fresh Related Questions
        register, purpose, email, venmo, prev_register = await self.getRegisterMember(member)

        insert_query = """
        insert into member (author_id, first_name, last_name, nickname, location, preferred_location, gender, pronounce, year_of_playing_vb, confident_position, formation, other, register, purpose, email, venmo, prev_register)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        await self.cursor.execute(insert_query, (str(member), first_name, last_name, nickname, str(location), str(preferred_location), str(gender), str(pronounce), year_of_playing_vb, str(confident_position), str(formation), str(other), str(register), purpose, email, venmo, str(prev_register)))
        await self.bot.db.commit()
        
        # Open Play manhattan, queens,new-jersy, bronx, brooklyn
        await self.set_permissions_member(member, channel_id=1166533138911076362, send_messages=False)
        await self.set_permissions_member(member, channel_id=1166543179252760668, send_messages=False)
        await self.set_permissions_member(member, channel_id=1166543213541216256, send_messages=False)
        await self.set_permissions_member(member, channel_id=1181709100132872253, send_messages=False)
        await self.set_permissions_member(member, channel_id=1185084178379837530, send_messages=False)
        # 活動專區/2024波紐馬
        await self.set_permissions_member(member, channel_id=1185224900630282282)
        # 聊天專區/閒聊
        await self.set_permissions_member(member, channel_id=1166544890386206812)
        # 聊天專區/排球比賽討論
        await self.set_permissions_member(member, channel_id=1166544930655711353)
        # 聊天專區/健身
        await self.set_permissions_member(member, channel_id=1173996775275778058)
        # 聊天專區/復健
        await self.set_permissions_member(member, channel_id=1173996804258402335)

        # 在 "新成員報到" channel 恭喜
        channel = self.bot.get_channel(1166533087493103668)
        select_query = """
        select
        *
        from member
        where first_name=? and last_name=? and nickname=?;"""

        self.cursor = await self.bot.db.cursor()
        await self.cursor.execute(select_query, (first_name, last_name, nickname))
        result = await self.cursor.fetchone()
        
        embed = self.embedProfile(result)

        await update_excel(channel, message_flag=False)

        await channel.send(f"恭喜 {nickname} 加入！歡迎！", embed=embed)


async def setup(bot):
    await bot.add_cog(Member(bot))