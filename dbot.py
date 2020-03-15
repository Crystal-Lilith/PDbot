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

    global nitro_red
    global nitro_green
    global nitro_blue
    nitro_red = randint(0,255)
    nitro_green = randint(0,255)
    nitro_blue = randint(0,255)

    pden = get(client.guilds, name="Programmer's Den")
    nitro_role = get(pden.roles, name='Server Booster')
    client.loop.create_task(rainbow_role(nitro_role))

async def rainbow_role(role):
    global nitro_red
    global nitro_green
    global nitro_blue
    color = discord.Color.from_rgb(nitro_red, nitro_green, nitro_blue)
    while True:
        await role.edit(colour=color)
        await update_color()
        await asyncio.sleep(4)
async def update_color():
    global nitro_red
    global nitro_green
    global nitro_blue
    if nitro_red > 254:
        nitro_red = 0
    else:
        nitro_red += 1
    if nitro_green > 254:
        nitro_green = 0
    else:
        nitro_green += 1
    if nitro_blue > 254:
        nitro_blue = 0
    else:
        nitro_blue += 1




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
