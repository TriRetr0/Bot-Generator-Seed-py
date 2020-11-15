import discord
from discord.ext import commands
from dotenv import load_dotenv
from settings import setsettings
import os
import sys
import re
import time
import requests
load_dotenv()
#intents = discord.Intents.default()
#intents.typing = True
#intents.presences = True
#intents.members = True
#client = commands.Bot(command_prefix = '!', intents=intents)
client = commands.Bot(command_prefix = '!')
client.remove_command("help")
OoTRV = open("OoT-Randomizer/version.py","r").read().split('\'')[1]
GeneRawzV = open(".version","r").read().split('\'')[1]
ROMPATH = os.getenv("ROMPATH")
OUTPATH = os.getenv("OUTPATH")



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))
    print(f"User {client.user} connected")
    print(os.getenv("ROMPATH"))



@client.command()
async def generate(ctx, settings="import", custom="N/A", spoil=True):
        OoTRV = open("OoT-Randomizer/version.py","r").read().split('\'')[1]
        if ctx.message.attachments and settings == "import":
            embedVar = discord.Embed(title="GeneRawz :", description=f"Generating import seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
            setsettings(ROMPATH, OUTPATH, "import")
        elif settings == "random":
            os.system("cd OoT-Randomizer && git checkout b670183e9aff520c20ac2ee65aa55e3740c5f4b4 && cd plando-random-settings && python3 PlandoRandomSettings.py && cd ../..")
            OoTRV = open("OoT-Randomizer/version.py","r").read().split('\'')[1]
            embedVar = discord.Embed(title="GeneRawz :", description=f"Generating random seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
            setsettings(ROMPATH, OUTPATH, "random")
        elif settings == "standard":
            setsettings(ROMPATH, OUTPATH)
            embedVar = discord.Embed(title="GeneRawz :", description=f"Generating standard seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
        elif settings == "custom":
            if custom == "N/A":
                embedVar = discord.Embed(title="ERROR:", description=f"```No settings string given```", color=0xff0000)
                await ctx.send(embed=embedVar)
                return
            else:
                setsettings(ROMPATH, OUTPATH, custom)
                embedVar = discord.Embed(title="GeneRawz :", description=f"Generating {custom} settings seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
        elif settings == "import":
            if custom == "N/A":
                embedVar = discord.Embed(title="ERROR:", description=f"```No settings provided```\nfor {ctx.author.mention}", color=0xff0000)
                await ctx.send(embed=embedVar)
                return
            else:
                embedVar = discord.Embed(title="GeneRawz :", description=f"Generating import seed in progress with OoTR: {OoTRV}\nfor {ctx.author.mention}")
                file = requests.get(custom)
                open("settings/settings.sav.import", "wb").write(file.content)
                setsettings(ROMPATH, OUTPATH, "import")
        else:
            embedVar = discord.Embed(title="ERROR:", description=f"```Unrecognized settings```\nfor {ctx.author.mention}", color=0xff0000)
            await ctx.send(embed=embedVar)
            return
        embedVar.set_footer(text=f"{GeneRawzV}, {OoTRV}")
        message = await ctx.send(embed=embedVar)
        print("Start Randomizer")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"!generate {settings}"))
        if settings != "custom":
            os.system('python3 OoT-Randomizer/OoTRandomizer.py')
        else:
            os.system(f'cd OoT-Randomizer/ && python3 OoTRandomizer.py --settings_string {custom} && cd ..')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Done."))
        print("Seed generated")
        embedVar = None
        if spoil == True:
            for file in os.listdir("OoT-Randomizer/Logs"):
                os.replace(f"OoT-Randomizer/Logs/{file}", f"{OUTPATH}/Generation logs")
            fileread = open(f"{OUTPATH}/Generation logs", "r")
            for line in fileread:
                if re.search("UNBEATABLE", line):
                    print("UNBEATABLE")
                    embedVar = discord.Embed(title="GeneRawz :", description=f":warning: Done. Settings: {settings}, {custom}\n```{line}```\nFiles generated :\nfor {ctx.author.mention}", color=0xffff00)
                elif re.search("Failed attempt 1 of 10: Entrance placement attempt count exceeded for world 0", line):
                    embedVar = discord.Embed(title="GeneRawz :", description=f":warning: Done. Settings: {settings}, {custom}\n```{line}```\nFiles generated :\nfor {ctx.author.mention}", color=0x0000ff)
                elif re.search("Not enough gossip stone locations for fixed hint type woth.", line):
                    embedVar = discord.Embed(title="GeneRawz :", description=f":no_entry_sign: Totally failed... Try again. Settings: {settings}, {custom}\n```{line}```\nFiles generated :\nfor {ctx.author.mention}", color=0xff0000)
                elif re.search("No more valid entrances to replace", line):
                    embedVar = discord.Embed(title="GeneRawz :", description=f":ok: Done. Settings: {settings}, {custom}\n```{line}```\nFiles generated :\nfor {ctx.author.mention}", color=0x0000ff)
            if embedVar == None:
                embedVar = discord.Embed(title="GeneRawz :", description=f":green_square: Done. Settings: {settings}, {custom}\nFiles generated :\nfor {ctx.author.mention}", color=0x00ff00)
        else:
            for file in os.listdir(f"{OUTPATH}"):
                if file.endswith(".json"):
                    os.remove(f"{OUTPATH}/{file}")
            embedVar = discord.Embed(title="GeneRawz :", description=f":spy: Done. No log spoil. Settings: {settings}, {custom}\nFiles generated :\nfor {ctx.author.mention}", color=0x888888)
        embedVar.set_thumbnail(url=f"{client.user.avatar_url}")
        embedVar.set_footer(text=f"{GeneRawzV}, {OoTRV}")
        await message.edit(embed=embedVar)


@client.command()
async def version(ctx):
    embedVar = discord.Embed(title="GeneRawz:", description=f"GeneRawz: [{GeneRawzV}](https://github.com/RawZ06/Bot-Generator-Seed-py)\nOoT Randomizer: [{OoTRV}](https://github.com/Roman971/OoT-Randomizer)")
    embedVar.set_thumbnail(url=f"{client.user.avatar_url}")
    await ctx.send(embed=embedVar)

@client.command()
@commands.has_permissions(administrator=True)
async def set_channel(ctx, Channel=None):
    if Channel == None:
        Channel = f"{ctx.channel.mention}"
    open(f"database/{ctx.guild.id}", "w").write(Channel.split("#")[1].split(">")[0])
    embedVar = discord.Embed(title="GeneRawz:", description=f"Now set in {Channel}")
    embedVar.set_thumbnail(url=f"{client.user.avatar_url}")
    await ctx.send(embed=embedVar)


@client.command()
async def help(ctx):
    embedVar = discord.Embed(title="HELP - GeneRawz", description=f"for {ctx.author.mention}")
    embedVar.set_thumbnail(url="https://img.icons8.com/bubbles/2x/help.png")
    embedVar.add_field(name="!help", value="Display this message", inline=True)
    embedVar.add_field(name="!version", value="Display bot and OoTR version", inline=True)
    embedVar.add_field(name="!set_channel", value="Set the bot channel to the current channel", inline=True)
    embedVar.add_field(name="!generate", value="Generate an OoT Randomizer seed. Usage: !generate [settings (standard, random, custom)] or upload a settings file", inline=False)
    embedVar.add_field(name="NO LOGS:", value="!generate random N/A False", inline=True)
    embedVar.add_field(name="SETTINGS FILE RULE:", value='Need to start with: ```json\n{\n    "rom": "",\n    "output_dir": "",\n    "enable_distribution_file": false,\n    ...```', inline=False)
    embedVar.add_field(name="BUGS:", value="If a random seed is not gived or after 20min, regenerate because the seed is mostly **unbeatable**", inline=False)
    embedVar.set_footer(text=f"{GeneRawzV}, {OoTRV}")
    await ctx.send(embed=embedVar)

@version.before_invoke
@help.before_invoke
@generate.before_invoke
async def on_command_call(ctx):
    if ctx.channel.id == int(open(f"database/{ctx.guild.id}", "r").read()) or ctx.guild == None:
        if ctx.message.attachments:
            print("Attachements detected. Can't delete")
            url = str(ctx.message.attachments[0]).split("'")[3].split("'")[0]
            file = requests.get(url)
            open("settings/settings.sav.import", "wb").write(file.content)
        else:
            if ctx.guild:
                print("Attachements not detected. Deleted")
                await ctx.message.delete()
        print("Command can be invoke here")
    else:
        raise Exception('Not allowed here')



@generate.after_invoke
async def on_generate_exit(ctx):
    area = ctx.message.channel
    for i in os.listdir(f"{OUTPATH}"):
        if os.path.isdir(f"{OUTPATH}/{i}"):
            continue
        os.replace(f"files/{i}", f"{OUTPATH}/{ctx.author.name} {i}")
        await ctx.send(file=discord.File(f'{OUTPATH}/{ctx.author.name} {i}'))
        os.remove(f'{OUTPATH}/{ctx.author.name} {i}')
    os.system("cd OoT-Randomizer && git checkout Dev-R")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))



@client.event
async def on_command_error(ctx, error):
    if ctx.channel.id == int(open(f"database/{ctx.guild.id}", "r").read()) or ctx.guild == None:
        embedVar = discord.Embed(title="ERROR:", description=f'```py\n{error}```\nfor {ctx.author.mention}, <@&764216400184737803>', color=0xff0000)
        embedVar.set_footer(text=f"!help for information\n{GeneRawzV}, {OoTRV}")
        await ctx.send(embed=embedVar)
        print(error)
        date = time.strftime("%d-%m-%Y")
        hour = time.strftime("%H-%M-%S")
        open("errlogs", "a").write(f"----------{date}|{hour}----------\n{error}\n")

client.run(os.getenv("TOKEN"))
