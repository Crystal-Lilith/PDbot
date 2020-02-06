import os, json, asyncio

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
                      status=discord.Status.idle, activity=discord.Game(name='Booting...'))

client.remove_command('help')

@client.listen
async def on_ready():
    print('Bot online!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Ready to program!'))

@client.event
async def on_ready():
    print('Bot online!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Ready!'))

@client.command()
async def help(ctx):
    cmds = []
    for command in client.commands:
        cmds.append(command.name)
    with open('./cmds/dcmds.json', 'w+') as f:
        json.dump(cmds, f)

for i in os.listdir('./cogs/dpy'):
    if i.endswith('.py'):
        with open(f"./cogs/dpy/{i}") as f:
            exec(f.read())

token = os.environ.get('TOKEN')
client.run(token)
