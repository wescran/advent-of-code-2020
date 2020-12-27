#!/usr/bin/env python3
import os
import discord

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

class AdventBot(discord.Client):
    async def on_ready(self):
        for guild in self.guilds:
            if guild.name == SERVER:
                break
        print(f"{self.user} is connected to the following guild:\n{guild.name}(id: {guild.id})")

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    async def on_message(self,message):
        pass

client = AdventBot()
client.run(TOKEN)
