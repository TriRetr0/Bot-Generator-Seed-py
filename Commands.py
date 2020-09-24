from Command import Command
from generate import generate_standard, generate_random, generate_custom


class Commands:

    def __init__(self):
        self.commands = {}
    
    def add_commands(self, command):
        self.commands[command.get_name()] = command
    
    async def execute(self, message, command_name, args):
        if(self.commands[command_name]):
            await self.commands[command_name].execute(message, args)
    
    def help_string(self):
        return '\n'.join(list(map(lambda c: c.help_string(), self.commands.values())))

commands = Commands()

async def print_help(message, args):
    await message.channel.send('{0.author.mention} Help :\n'.format(message) + commands.help_string())

async def print_version(message, args):
    f = open("./OoT-Randomizer/version.py", "r")
    await message.channel.send(f.read().split('\'')[1])
    f.close()

commands.add_commands(Command("!help", "Affiche l'aide", None, print_help))
commands.add_commands(Command("!genstandard", "Generate standard seed", None, generate_standard))
commands.add_commands(Command("!genrandom", "Generate random settings seed", None, generate_random))
commands.add_commands(Command("!generate", "Generate a custom settings seed", None, generate_custom))
commands.add_commands(Command("!version", "Print version roman's fork", None, print_version))