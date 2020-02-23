from hata import eventlist, enter_executor
from urllib.request import urlopen

commands = eventlist()

@commands
async def ip(client, message):
    if message.author.id in [562086061153583122, 300126997718237195, 207188318130012160, 524288464422830095]:
        async with enter_executor():
            client.loop.create_task_threadsafe(client.message_create(message.channel, f"Bot's public IP is {urlopen('http://icanhazip.org').read().decode('utf-8').rstrip()}"))
