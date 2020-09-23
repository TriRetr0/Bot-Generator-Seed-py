from Command import Command
from generate import generate_standard, generate_random

class Commands:

    def __init__(self):
        self.commands = {}
    
    def add_commands(self, command):
        self.commands[command.get_name()] = command
    
    async def execute(self, message, command_name):
        if(self.commands[command_name]):
            await self.commands[command_name].execute(message)
    
    def help_string(self):
        return '\n'.join(list(map(lambda c: c.help_string(), self.commands.values())))

commands = Commands()

async def print_help(message):
    await message.channel.send('{0.author.mention} Help :\n'.format(message) + commands.help_string())

commands.add_commands(Command("!help", "Affiche l'aide", None, print_help))
commands.add_commands(Command("!genstandard", "Generate standard seed", None, generate_standard))
commands.add_commands(Command("!genrandom", "Generate random settings seed", None, generate_random))