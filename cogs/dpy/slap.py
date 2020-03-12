@client.command()
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('$slap'):
        msg = f”*Slapped* {ctx.author.mention}”
        await ctx.channel.send(msg)