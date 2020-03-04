import os, json, asyncio, threading
from random import randint
from pdaddons.python.hata.interpreter import Interpreter
from pdaddons.python.hata.extension_loader import EXTENSION_LOADER
from pdaddons.python.hata.ext import HelpPages

import discord, requests, random, pyfiglet
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
from hata import Client, start_clients, events, Embed, enter_executor
from hata.events import Pagination, ReactionAddWaitfor, ReactionDeleteWaitfor
from hata.extension_loader import ExtensionLoader, ExtensionError

prefix = os.environ.get('PREFIX')
token = os.environ.get('TOKEN')

pdbot = Client(token)

on_command = pdbot.events(events.CommandProcesser(prefix)).shortcut

client = commands.Bot(command_prefix=os.environ.get('PREFIX'), case_insensitive=True, description='PDBot - v 0.9.0', 
                        status=discord.Status.idle, activity=discord.Game(name='Compiling'))

client.remove_command('help')

pdbot.events(ReactionAddWaitfor)
pdbot.events(ReactionDeleteWaitfor)

EXTENSION_LOADER(pdbot).load_all().syncwrap().wait()

@on_command(case='update')
async def restart_bot(client, message):
    await client.message_create(message.channel, "Updating bot...")
    os.system('sh stop.sh')

@on_command
async def help(client, message, content):
    if content not in [None, '']:
        return
    await Pagination(client, message.channel, HelpPages(client, message))

@client.listen()
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='~$ ./PDBot'))

@client.command()
async def help(ctx):
    cmds = {}
    with open('./cmds/dcmds.json', 'w') as f:
        for command in client.commands:
            desc = command.description.split('||')
            if command.name != "help":
                cmds[command.name] = {"desc": desc[0], 'syntax': desc[-1], 'required_roles': [], 'required_perms': []}
        json.dump(cmds, f)
        f.close()

for i in os.listdir('./cogs/dpy'):
    if i.endswith('.py'):
        with open(f"./cogs/dpy/{i}") as f:
            exec(f.read())

on_command(Interpreter(locals().copy()), case='execute')

PDBot = pdbot

def hrun():
    os.system("python3 .hworkaround.py")
  
threading.Thread(target=hrun()).start()
client.run(token)
