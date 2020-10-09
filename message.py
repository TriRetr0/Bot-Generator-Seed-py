import time
import discord

def log(content):
    if(not content):
        return
    date = time.strftime("%d-%m-%Y")
    hour = time.strftime("%H-%M-%S")
    f = open("./logs/" + date + "_logfile.txt", "a")
    f.write("["+ date + "-" + hour + "] " + content + "\n")
    f.close()

async def print_send(message, content):
    print(content)
    embedVar = discord.Embed(title="GeneRawz", description=f"{content}\n\nfor {message.author.mention}")
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/753907038035247194/f5de60765226054bc282234501a807f7.webp?size=64")
    embedVar.set_footer(text="1.1 Dev")
    msg = await message.channel.send(embed=embedVar)
    log(content)

async def print_embed(message, content):
    print(content)
    await message.channel.send(content + '\n')
    log(content)

async def print_reply(message, content):
    print(content)
    await message.channel.send('{0.author.mention} '.format(message) + content + '\n')
    log(content)

async def print_not_send(message, content):
    print(content)
    log(content)
