from hata import eventlist
import subprocess.getoutput

commands = eventlist()

@commands
async def ip(client, message):
    if message.author.id in [562086061153583122, 300126997718237195, 207188318130012160, 524288464422830095]:
        await client.message_create(message.channel, subprocess.getoutput("curl icanhazip.com"))
