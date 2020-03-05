import os
import json

import json
from .hata import Client, start_clients, events, Embed, enter_executor
from .hata.events import Pagination, ReactionAddWaitfor, ReactionDeleteWaitfor
from .hata.extension_loader import ExtensionLoader, ExtensionError

from pdaddons.python.hata.interpreter import Interpreter

token = os.environ.get('TOKEN')
pdbot = Client(token)

prefix = os.environ.get('PREFIX')
on_command = pdbot.events(events.CommandProcesser(prefix)).shortcut
del(prefix)
pdbot.events(ReactionAddWaitfor)
pdbot.events(ReactionDeleteWaitfor)


EXTENSION_LOADER = ExtensionLoader(pdbot)

def add_extensions():
    async def entry(client, lib):
        commands=getattr(lib,'commands',None)
        if commands is not None:
            pdbot.events.message_create.shortcut.extend(commands)
        
        entry=getattr(lib,'entry',None)
        if entry is not None:
            if is_coro(entry):
                await entry(client)
            else:
                entry(client)
            
        print(f'Hata: {lib.__name__} extension has been loaded!')
        
    async def exit(client, lib):
        commands=getattr(lib,'commands',None)
        if commands is not None:
            pdbot.events.message_create.shortcut.unextend(commands)
        
        exit=getattr(lib,'exit',None)
        if exit is not None:
            if is_coro(exit):
                await exit(client)
            else:
                exit(client)

        print(f'Hata: {lib.__name__} extension has been unloaded!')

    for filename in os.listdir('./cogs/hata/'):
        if filename.endswith('.py'):
            module_name='cogs.hata.'+filename[:-3]
            EXTENSION_LOADER.add(module_name, entry_point=entry, exit_point=exit)

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
        cmds.append(i.name)
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
