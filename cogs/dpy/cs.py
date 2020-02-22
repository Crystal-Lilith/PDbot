@client.command(description='Changes bot status')
@commands.has_role('PDBot Dev')
async def cs(ctx, status, *, desc):
    if status == 'game' or status == 'stream':
        if status == 'game':
            await client.change_presence(activity=discord.Game(name=desc))
        if status == 'stream':
            await client.change_presence(activity=discord.Streaming(name=desc))
        await ctx.channel.send('Bot status changed!')
    else:
        print('Not a valid status!')
