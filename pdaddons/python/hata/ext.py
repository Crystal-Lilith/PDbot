from hata import Embed
from os import listdir
from json import load as jload
def HelpPages(client, message):
    cmds = []
    for i in client.events.message_create.commands:
        cmds.append(i)
    for y in listdir('cmds/'):
        with open('cmds/'+y,) as f:
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
    return result
