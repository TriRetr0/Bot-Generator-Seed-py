import discord
from dotenv import load_dotenv
import os
load_dotenv()
from message import print_not_send

from Commands import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        channels_allowed = os.getenv("CHANNELS").split(',')
        if not message.channel.name in channels_allowed:
            return

        command = message.content.split(" ")[0]
        args = " ".join(message.content.split(" ")[1:])
        print_not_send(message, message.author.name + ": " + message.content)
        await commands.execute(message, command, args)

client = MyClient()
client.run(os.getenv("TOKEN"))