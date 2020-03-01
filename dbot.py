import os, json, asyncio, threading
from random import randint

while True:
    try:
        import discord, requests, random
        from discord.ext import commands
        from discord.utils import get
        from bs4 import BeautifulSoup
        from flask import Flask, request
        from gevent.pywsgi import WSGIServer
        break
    except:
        os.system('pip3 install -r requirements.txt')



client = commands.Bot(command_prefix=os.environ.get('PREFIX'), case_insensitive=True, description='PDBot - v 0.9.0', 
                        status=discord.Status.idle, activity=discord.Game(name='Compiling'))

client.remove_command('help')


@client.event
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

token = os.environ.get('TOKEN')

app=Flask("Private API")

@app.route("/guild_count", methods=['GET'])
def guild_count():
    if request.method != 'GET':
        return f'You have to use GET requests not {str(request.method)} requests!'
    return str(len(client.guilds))


threading.Thread(target=WSGIServer, args=((('0.0.0.0',9010), app).serve_forever()).start()
client.run(token)
