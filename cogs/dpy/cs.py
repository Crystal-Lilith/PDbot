@client.command(description='Changes bot status')
@commands.has_role('PDBot Dev')
async def cs(ctx, *, desc):
    await client.change_presence(activity=discord.Game(name=desc))
    await ctx.channel.send('Bot status changed!')
