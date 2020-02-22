@client.command(description='Changes bot status')
@command.has_role('PDBot Dev')
async def cs(ctx, *, status):
    await client.change_presence(activity=discord.CustomActivity(name=status))
    await ctx.channel.send('Bot status changed!')
