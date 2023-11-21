import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        

def run_discord_bot():
    TOKEN = 'MTE3NTUxMzIwNjk3NDg2MTMyMw.GjGiwL.kEhFX2GwLLKsbJOi2EfKfEoM2K_iAmhM5Vmwxg'
    intents = discord.Intents.all()
    discord.member = True
    # bot = commands.Bot(command_prefix="[",intents = intents)
    # intents = discord.Intents.default()
    intents.message_content = True  
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("{} is now running!".format(client.user))

    @client.event
    async def on_member_join(member):
        await member.send('歡迎加入Fresh!, 請填寫問卷已開啟頻道！')
        await member.send("請開始填寫問卷:")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print("{} said: {}, ({})".format(username, user_message, channel))

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

