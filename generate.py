import discord
from settings import setsettings

@client.command()
async def generate(ctx, settings, custom="N/A"):
    await ctx.message.delete()
    if ctx.channel.id == CHANNELSID or ctx.guild == None:
        for dir, sub_dirs, files in os.walk("files"):
            if files:
                embedVar = discord.Embed(title="GeneRawz :", description=f"**Sorry, another seed is being generated**\nfor {ctx.author.mention}")
                print("Someone has called !generate but another seed is being generated")
                return


        if settings == "random":
            os.system("cd OoT-Randomizer/plando-random-settings/ && python3 PlandoRandomSettings.py && cd ../..")
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
        print('Seed removed')

