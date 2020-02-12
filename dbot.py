import os, json, asyncio
from random import randint

try:
    import discord
    from discord.ext import commands
    from discord.utils import get
except:
    os.system('pip3 install discord')
    import discord
    from discord.ext import commands
    from discord.utils import get


client = commands.Bot(command_prefix=os.environ.get('PREFIX'), case_insensitive=True, description='PDBot - v 0.9.0', 
                      status=discord.Status.idle, activity=discord.Game(name='Compiling'))

client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='~$ ./PDBot'))

@client.command()
async def help(ctx):
    cmds = {}
    for command in client.commands:
        desc = {"desc":command.description, "perms":[], "roles":[]} #We need a way to fill in perms, maybe a perm handler?
        cmds[command.name] = desc
    with open('./cmds/dcmds.json', 'w+') as f:
        json.dump(cmds, f)

for i in os.listdir('./cogs/dpy'):
    if i.endswith('.py'):
        with open(f"./cogs/dpy/{i}") as f:
            exec(f.read())

token = os.environ.get('TOKEN')
client.run(token)
