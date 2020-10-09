import process
import sys
import discord
from message import print_send, print_reply, print_not_send
__basedir = sys.path[0]

async def generate(message):
    await print_not_send(message, "Start Randomizer")
    res = process.execute("python3 "+ __basedir +"/OoT-Randomizer/OoTRandomizer.py")
    await print_not_send(message, res)
    await print_not_send(message, "Seed generated")
    files = list(filter(lambda file: file, process.execute("ls "+ __basedir +"/files").split("\n")))
    await print_send(message, "Files genereted :")
    path_files = list(map(lambda file: (__basedir + "/files/" + file), files))
    for file in path_files:
        await message.channel.send(file=discord.File(file))
    process.execute("rm "+ __basedir +"/files/*.json" + " " + __basedir +"/files/*.zpf")
    await print_not_send(message, 'Seed removed')

async def generate_standard(message, args):
    await print_send(message, "Generate seed with settings : standard")
    await print_not_send(message, "Copying settings file into randomizer")
    process.execute("cp "+ __basedir +"/settings/settings.sav.std" + " " + __basedir +"/OoT-Randomizer/settings.sav")
    await print_not_send(message, "Settings file copied")
    await generate(message)

async def generate_random(message, args):
    await print_send(message, "Generating random seed in progress")
    await print_not_send(message, "Generating random settings")
    process.execute("cd OoT-Randomizer/plando-random-settings; python3 PlandoRandomSettings.py; cd ../..")
    await print_not_send(message, "Random settings generated")
    await print_not_send(message, "Copying settings file into randomizer")
    process.execute("cp "+ __basedir +"/settings/settings.sav.ran" + " " + __basedir +"/OoT-Randomizer/settings.sav")
    await print_not_send(message, "Settings file copied")
    await generate(message)

async def generate_custom(message, args):
    if(not args):
        await print_send(message, "Nothing settings specified")
        return
    await print_send(message, "Generate seed with settings : " + args)
    await print_not_send(message, "Generating standard seed in progress")
    await print_not_send(message, "Copying settings file into randomizer")
    process.execute("cp "+ __basedir +"/settings/settings.sav.std" + " " + __basedir +"/OoT-Randomizer/settings.sav")
    await print_not_send(message, "Settings file copied")
    await print_not_send(message, "Start Randomizer")
    res = process.execute("python3 "+ __basedir +"/OoT-Randomizer/OoTRandomizer.py --settings_string " + args)
    await print_not_send(message, res)
    await print_not_send(message, "Seed generated")
    files = list(filter(lambda file: file, process.execute("ls "+ __basedir +"/files").split("\n")))
    await print_reply(message, "Files genereted :")
    path_files = list(map(lambda file: (__basedir + "/files/" + file), files))
    for file in path_files:
        await message.channel.send(file=discord.File(file))
    process.execute("rm "+ __basedir +"/files/*.json" + " " + __basedir +"/files/*.zpf")
    await print_not_send(message, 'Seed removed')
