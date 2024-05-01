import discord
import os
from dotenv import load_dotenv
import bot

load_dotenv()
discord_key = os.getenv('TOKEN')
print(discord_key)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#your bot id
my_bot_id = int(os.getenv('BOT_ID'))
owr_id = int(os.getenv('MY_ID'))

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    message_id = message.author.id
    if message_id != my_bot_id and message_id != owr_id:
        response = message.content
        print(response)
        if isinstance(message.channel, discord.TextChannel) and message.channel.name == 'get-code':
            final_ans = bot.get_response(response)
            await message.channel.send(final_ans)

                    
client.run(discord_key)