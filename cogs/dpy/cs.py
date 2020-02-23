@client.command(description='Changes bot status')
@commands.has_role('PDBot Dev')
async def cs(ctx, mode, *, desc):
    if mode == 'static' or mode == 'dynamic':
        if mode == 'static':
            await client.change_presence(activity=discord.Game(name=desc))
            await ctx.channel.send('Bot status changed!')
        if mode == 'dynamic':
            desc = desc.split()
            await ctx.channel.send('Bot status changed!')
            while True:
                for i in desc:
                    await client.change_presence(activity=discord.Game(name=i))
                    asyncio.sleep(50)
