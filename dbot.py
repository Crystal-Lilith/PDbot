import os, json, asyncio, threading
from random import randint

import discord, requests, random, pyfiglet
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
from flask import Flask, request

client = commands.Bot(command_prefix=os.environ.get('PREFIX'), case_insensitive=True, description='PDBot - v 0.9.0', 
                        status=discord.Status.idle, activity=discord.Game(name='Compiling'))

client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='~$ ./PDBot'))
    nitro_role = await Client.fetch_guild(668000598221651975).get_role(674833235238322187)
    client.loop.create_task(rainbow_role(nitro_role))

async def rainbow_role(role):
    class RandColors:
        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        async def __init__(self):
            if RandColors.red > 254:
                RandColors.red = 0
            else:
                RandColors.red += 1
            if RandColors.green > 254:
                RandColors.green = 0
            else:
                RandColors.green += 1
            if RandColors.blue > 254:
                RandColors.blue = 0
            else:
                RandColors.blue += 1

    color = discord.Color.from_rgb(RandColors.red, RandColors.green, RandColors.blue)
    while True:
        await role.edit(colour=color)
        await asyncio.sleep(4)


@client.command()
async def help(ctx):
    cmds = {}
    with open('./cmds/dcmds.json', 'w') as f:
        for command in client.commands:
            desc = command.description.split('||')
            if command.name != 'help':
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


# threading.Thread(target=WSGIServer, args=((('0.0.0.0',9010), app).serve_forever()).start())
client.run(token)
