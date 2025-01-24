import discord
from discord.ext import tasks

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.send_message.start()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

    @tasks.loop(minutes=120)
    async def send_message(self, message):
        channel = self.get_channel(1317173616843952178)  # replace YOUR_CHANNEL_ID with the actual channel ID
        if channel:
            await message.channel.send('/bump')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client.run('MTMzMjM4NDIzMjM5NTM3ODg0MQ.Gla1Ht.VjhApFutE2T_h6Aut8-feGgOSbitBrgtEZyYqY')
