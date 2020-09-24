import process
import sys
import discord
__basedir = sys.path[0]

async def print_send(message, content):
    print(content)
    await message.channel.send(content + '\n')

async def print_reply(message, content):
    print(content)
    await message.channel.send('{0.author.mention} '.format(message) + content + '\n')

async def generate(message, args):
    await print_send(message, "Start Randomizer")
    process.execute("python3 "+ __basedir +"/OoT-Randomizer/OoTRandomizer.py")
    await print_send(message, "Seed generated")
    files = list(filter(lambda file: file, process.execute("ls "+ __basedir +"/files").split("\n")))
    await print_reply(message, "Files genereted :")
    path_files = list(map(lambda file: (__basedir + "/files/" + file), files))
    for file in path_files:
        await message.channel.send(file=discord.File(file))
    process.execute("rm "+ __basedir +"/files/*.json" + " " + __basedir +"/files/*.zpf")
    await print_send(message, 'Seed removed')

async def generate_standard(message, args):
    await print_send(message, "Generating standard seed in progress")
    await print_send(message, "Copying settings file into randomizer")
    process.execute("cp "+ __basedir +"/settings/settings.sav.std" + " " + __basedir +"/OoT-Randomizer/settings.sav")
    await print_send(message, "Settings file copied")
    await generate(message)

async def generate_random(message, args):
    await print_send(message, "Generating standard seed in progress")
    await print_send(message, "Generating random settings")
    process.execute("cd OoT-Randomizer/plando-random-settings; python3 PlandoRandomSettings.py; cd ../..")
    await print_send(message, "Random settings generated")
    await print_send(message, "Copying settings file into randomizer")
    process.execute("cp "+ __basedir +"/settings/settings.ran.std" + " " + __basedir +"/OoT-Randomizer/settings.sav")
    await print_send(message, "Settings file copied")
    await generate(message)

async def generate_custom(message, args):
    await print_send(message, "Generate seed with settings : " + args)
    await print_send(message, "Generating standard seed in progress")
    await print_send(message, "Copying settings file into randomizer")
    process.execute("cp "+ __basedir +"/settings/settings.sav.std" + " " + __basedir +"/OoT-Randomizer/settings.sav")
    await print_send(message, "Settings file copied")
    await print_send(message, "Start Randomizer")
    process.execute("python3 "+ __basedir +"/OoT-Randomizer/OoTRandomizer.py --settings_string " + args)
    await print_send(message, "Seed generated")
    files = list(filter(lambda file: file, process.execute("ls "+ __basedir +"/files").split("\n")))
    await print_reply(message, "Files genereted :")
    path_files = list(map(lambda file: (__basedir + "/files/" + file), files))
    for file in path_files:
        await message.channel.send(file=discord.File(file))
    process.execute("rm "+ __basedir +"/files/*.json" + " " + __basedir +"/files/*.zpf")
    await print_send(message, 'Seed removed')