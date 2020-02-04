import os
import subprocess

from hata import eventlist, Embed, alchemy_incendiary
from hata.events import ContentParser, Pagination
from hata.extension_loader import ExtensionError

commands = eventlist()

def OIDs():
    return [207188318130012160, 300126997718237195, 524288464422830095, 562086061153583122]

@commands(case='cog-list')
async def list_of_cogs(client, message, content):
    cogs = []
    for i in os.listdir(os.path.join('cogs', 'hata')):
        if i.endswith('.py'):
            cogs.append(i[:-3])
    pages=[]
    part=[]
    index=0
    for element in cogs:
        if index==15:
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
        embed=Embed('Cogs:',color='029320',description=pages[index])
        index+=1
        embed.add_field('Cog-list',f'page {index} out of {limit}')
        result.append(embed)

    del pages
    await Pagination(client,message.channel,result)

@commands(case='update-cog')
@ContentParser('str, mode=2*')
async def update_cog(client, message, cog_name, cog_link):
    if message.author.id not in OIDs():
        return
    
    cog_name = cog_name.replace('.py','')
    
    await client.message_create(message.channel,f'Updating {cog_name}...')

    await client.loop.run_in_executor(alchemy_incendiary(
        subprocess.call,
        (f'cd {os.path.join("cogs", "hata")} && wget -O {cog_name}.py {cog_link}',),
        {'shell':True},))
    
    await client.message_create(message.channel,
        f'{cog_name} has successfully been updating\nReloading cog...')
    
    await client.extension_loader.reload(f'cogs.hata.{cog_name}')
    
    await client.message_create(message.channel,f'The cog {cog_name} has successfully been reloaded!')

@commands(case='remove-cog')
@ContentParser('str',)
async def remove_cog(client, message, cog_name):
    if message.author.id not in OIDs():
        return
    
    cog_name = cog_name.replace('.py','')
    await client.message_create(message.channel,'Unloading cog...')
    
    await client.extension_loader.unload(f'cogs.hata.{cog_name}')
    
    await client.message_create(message.channel,
        f'The cog {cog_name} has successfully been unloaded!\nremoving {cog_name}...')

    await client.loop.run_in_executor(alchemy_incendiary(
        subprocess.call,
        (f'cd {os.path.join("cogs", "hata")} && rm {cog_name}.py',),
        {'shell':True},))
    
    await client.message_create(message.channel,f'{cog_name} has successfully been deleted')

@commands
@ContentParser('str',)
async def load(client, message, extension):
    if message.author.id not in OIDs():
        return
    
    await client.message_create(message.channel,f'Loading {extension}...')
    await client.extension_loader.load(f'cogs.hata.{extension}')
    await client.message_create(message.channel,f'{extension} has been loaded!')


@commands
@ContentParser('str',)
async def reload(client, message, extension):
    if message.author.id not in OIDs():
        return
    await client.message_create(message.channel,f'Reloading {extension}...')
    await client.extension_loader.reload(f'cogs.hata.{extension}')
    await client.message_create(message.channel,f'{extension} has been reloaded!')


@commands
@ContentParser('str',)
async def unload(client, message, extension):
    if message.author.id not in OIDs():
        return
    await client.message_create(message.channel,f'unloading {extension}...')
    await client.extension_loader.unload(f'cogs.{extension}')
    await client.message_create(message.channel,f'{extension} has been unloaded!')

@commands
async def restart(client, message, content):
    if message.author.id not in OIDs():
        await client.message_create(message.channel,'You are not allowed to do this!')
        return
    
    await client.message_create(message.channel,'Restarting the bot now...')
    try:
        await client.extension_loader.reload_all()
    except ExtensionError as err:
        await Pagination(client, message.channel, [Embed('An extension raised:',content) for content in err.messages])
    else:
        await client.message_create(message.channel,'Done!')