from hata.extension_loader import ExtensionLoader, ExtensionError
from os import listdir

EXTENSION_LOADER = ExtensionLoader(client)

def add_extensions():
    EXTENSION_LOADER = ExtensionLoader(client)
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

    for filename in listdir('cogs/hata/'):
        if filename.endswith('.py'):
            module_name='cogs.hata.'+filename[:-3]
            EXTENSION_LOADER.add(module_name, entry_point=entry, exit_point=exit)
