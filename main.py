import discord
from discord.ext import commands
from dotenv import load_dotenv
from settings import setsettings
import os
import sys
import time
load_dotenv()
#intents = discord.Intents.default()
#intents.typing = True
#intents.presences = True
#intents.members = True
#client = commands.Bot(command_prefix = '!', intents=intents)
client = commands.Bot(command_prefix = '!')

client.remove_command("help")

GeneRawzV = open(".version","r").read().split('\'')[1]
OoTRV = open("OoT-Randomizer/version.py","r").read().split('\'')[1]
ROMPATH = os.getenv("ROMPATH")
OUTPATH = os.getenv("OUTPATH")
CHANNELSID = int(os.getenv("CHANNELSID"))



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))
    print(f"User {client.user} connected")
    print(os.getenv("CHANNELSID"))
    print(os.getenv("ROMPATH"))



@client.command()
async def generate(ctx, settings, custom="N/A"):
    await ctx.message.delete()
    if ctx.channel.id == CHANNELSID or ctx.guild == None:
        OoTRV = open("OoT-Randomizer/version.py","r").read().split('\'')[1]
        for dir, sub_dirs, files in os.walk("files"):
            if files:
                embedVar = discord.Embed(title="GeneRawz :", description=f"**Sorry, another seed is being generated**\nfor {ctx.author.mention}")
                print("Someone has called !generate but another seed is being generated")
        if settings == "random":
            os.system("cd OoT-Randomizer && git checkout 6fe41cac9b324897ab8f0344bd337a54a0da6f35 && cd plando-random-settings && python3 PlandoRandomSettings.py && cd ../..")
            OoTRV = open("OoT-Randomizer/version.py","r").read().split('\'')[1]
            embedVar = discord.Embed(title="GeneRawz :", description=f"Generating random seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
            setsettings(ROMPATH, OUTPATH, "random")
        elif settings == "standard":
            setsettings(ROMPATH, OUTPATH)
            embedVar = discord.Embed(title="GeneRawz :", description=f"Generating standard seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
        elif settings == "custom":
            if custom == "N/A":
                embedVar = discord.Embed(title="ERROR:", description=f"```No settings string given```")
                await ctx.send(embed=embedVar)
                return
            else:
                setsettings(ROMPATH, OUTPATH, custom)
                embedVar = discord.Embed(title="GeneRawz :", description=f"Generating {custom} settings seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
        else:
            embedVar = discord.Embed(title="ERROR:", description=f"```unrecognized settings```\nfor {ctx.author.mention}")
            return
        embedVar.set_footer(text=f"{GeneRawzV}, {OoTRV}")
        message = await ctx.send(embed=embedVar)
        print("Start Randomizer")
        if custom == "N/A":
            os.system('python3 OoT-Randomizer/OoTRandomizer.py')   
        else:
            os.system('cd OoT-Randomizer/ && python3 OoTRandomizer.py --settings_string {custom} && cd ..')
        print("Seed generated")
        embedVar = discord.Embed(title="GeneRawz :", description=f"Done. Settings: {settings}, {custom}\nFiles generated :\nfor {ctx.author.mention}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/753907038035247194/f5de60765226054bc282234501a807f7.webp?size=64")
        embedVar.set_footer(text=f"{GeneRawzV}, {OoTRV}")
        await message.edit(embed=embedVar)
        area=ctx.message.channel
        for i in os.listdir("files"):
            if os.path.isdir(f"files/{i}"):
                continue
            os.replace(f"files/{i}", f"files/{ctx.author.name} {i}")
            await ctx.send(file=discord.File(f'files/{ctx.author.name} {i}'))
            os.remove(f'files/{ctx.author.name} {i}')
        if open("OoT-Randomizer/version.py","r").read().split('\'')[1] == "5.2.65 R-6":
            os.system("cd OoT-Randomizer && git checkout Dev-R ; cd ..")
            OoTRV = open("OoT-Randomizer/version.py","r").read().split('\'')[1]
        print('Seed removed')



@client.command()
async def help(ctx):
    await ctx.message.delete()
    if ctx.channel.id == CHANNELSID or ctx.guild == None:
        embedVar = discord.Embed(title="HELP - GeneRawz", description=f"for {ctx.author.mention}")
        embedVar.set_thumbnail(url="https://img.icons8.com/bubbles/2x/help.png")
        embedVar.add_field(name="!help", value="Display this message", inline=True)
        embedVar.add_field(name="!generate", value="Generate an OoT Randomizer seed. Usage: !generate [settings (standard(weekly), random, custom, s4)]", inline=True)
        embedVar.set_footer(text=f"{GeneRawzV}, {OoTRV}")
        await ctx.send(embed=embedVar)



@client.command()
async def version(ctx):
    await ctx.message.delete()
    if ctx.channel.id == CHANNELSID or ctx.guild == None:
        embedVar = discord.Embed(title="GeneRawz:", description=f"GeneRawz: {GeneRawzV}, {OoTRV}\nOoT Randomizer: {OoTRV}")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/753907038035247194/f5de60765226054bc282234501a807f7.webp?size=64")
        await ctx.send(embed=embedVar)



@client.event
async def on_command_error(ctx, error):
    if ctx.channel.id == CHANNELSID or ctx.guild == None:
        embedVar = discord.Embed(title="ERROR:", description=f'```py\n{error}```\nfor {ctx.author.mention}, <@&764216400184737803>')
        embedVar.set_footer(text=f"!help for information\n{GeneRawzV}, {OoTRV}")
        await ctx.send(embed=embedVar)
        print(error)
        date = time.strftime("%d-%m-%Y")
        hour = time.strftime("%H-%M-%S")
        open("errlogs", "a").write(f"----------{date}|{hour}----------\n{error}\n")



client.run(os.getenv("TOKEN"))
