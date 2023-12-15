import bot
import os
from dotenv import load_dotenv

if __name__=='__main__':
  load_dotenv()
  TOKEN = os.getenv('DISCORD_TOKEN')
  client = bot.CustomClient()
  client.run(TOKEN)