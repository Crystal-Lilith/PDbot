@client.command(description='Changes bot status')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def cs(ctx, mode, *, desc):
    global bot_status_task
    if mode == 'static' or mode == 'dynamic':
        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0), description='Bot status changed!')
        embed.set_footer(text=f'Status changed by: {ctx.message.author}')
        if 'bot_status_task' in globals():
            bot_status_task.cancel()
        if mode == 'static':
            await client.change_presence(activity=discord.Game(name=desc))
            await ctx.channel.send(embed=embed)
        elif mode == 'dynamic':
            desc = desc.split()
            await ctx.channel.send(embed=embed)
            bot_status_task = client.loop.create_task(status_task(desc))
    else:
        embed = discord.Embed(title='Error!', color=discord.Color.from_rgb(255, 255, 51),
                                description='Not a valid mode!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)

async def status_task(desc):
    while True:
        for i in desc:
            await client.change_presence(activity=discord.Game(name=i))
            await asyncio.sleep(1.5)
