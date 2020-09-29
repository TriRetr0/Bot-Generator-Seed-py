import time

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
    await message.channel.send(content + '\n')
    log(content)

async def print_reply(message, content):
    print(content)
    await message.channel.send('{0.author.mention} '.format(message) + content + '\n')
    log(content)

async def print_not_send(message, content):
    print(content)
    log(content)