class Command:

    def __init__(self, name, description, roles, callback):
        self.name = name
        self.description = description
        self.roles = roles
        self.callback = callback
    
    def get_name(self):
        return self.name
    
    async def execute(self, message):
        roles = list(map(lambda a: a.name, message.author.roles))
        if not self.roles or all(elem in self.roles for elem in roles):
            await self.callback(message)
        else:
            await message.channel.send('{0.author.mention} Vous pouvez pas utiliser cette commande !'.format(message))
    
    def help_string(self):
        return '[' + (','.join(self.roles) if self.roles else "everyone")  + '] ' + self.name + ' : ' + self.description
