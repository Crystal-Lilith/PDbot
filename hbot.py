import os
import json

try:
    import hata, flask
    del(hata, flask)
except:
    os.system('pip3 install https://github.com/HuyaneMatsu/hata/archive/master.zip flask')

from hata import Client, start_clients, events, Embed, enter_executor
from hata.events import Pagination, ReactionAddWaitfor, ReactionDeleteWaitfor
from hata.extension_loader import ExtensionLoader, ExtensionError

from pdaddons.python.hata.interpreter import Interpreter

pdbot = Client(token)

on_command = pdbot.events(events.CommandProcesser(prefix)).shortcut

pdbot.events(ReactionAddWaitfor)
pdbot.events(ReactionDeleteWaitfor)

add_extensions()
EXTENSION_LOADER.load_all().syncwrap().wait()

@on_command(case='update')
async def restart_bot(client, message):
    await client.message_create(message.channel, "Updating bot...")
    os.system('sh stop.sh')

@on_command
async def help(client, message, content):
    if content not in [None, '']:
        return
    cmds = []
    for i in pdbot.events.message_create.commands:
        cmds.append(i)
    for y in os.listdir('./cmds/'):
        with open('./cmds/'+y, 'r') as f:
            x = json.load(f)
        for i in x:
            if i.lower() != 'help':
                cmds.append(i)
    cmds = sorted(cmds, key=str.lower) # Key positional argument is used to make sure uppercase commands don't take precedence.
    pages=[]
    part=[]
    index=0
    for element in cmds:
        if index==16:
            pages.append('\n'.join(part))
            part.clear()
            index=0
        part.append(f'**>>** {element}')
        index+=1

    pages.append('\n'.join(part))

    del part

    result=[]

    limit=len(pages)
    index=0
    while index<limit:
        embed=Embed('Commands:',color='029320',description=pages[index])
        index+=1
        embed.add_field("Do $meme for some funny memes!", f'page {index}/{limit}')
        result.append(embed)

    del pages
    await Pagination(client, message.channel,result)

on_command(Interpreter(locals().copy()), case='execute')

start_clients()
