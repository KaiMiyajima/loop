import time
import asyncio
from discord.ext import commands
import os
import traceback
import discord
from discord.ext import tasks
import asyncio


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 803619260349677589  # チャンネルID


# 接続に必要なオブジェクトを生成
client = discord.Client()


@client.event
async def on_ready():
    while True:
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('時間だよ')
        await asyncio.sleep(10)

client.run(token)
