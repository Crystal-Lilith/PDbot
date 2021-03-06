@client.command(description='Changes bot status||<static/dynamic> <desc>')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def cs(ctx, mode, *, desc):
    global bot_status_task
    if mode == 'static' or mode == 'dynamic':
        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0), description='Bot status changed!')
        embed.set_footer(text=f'Status changed by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        if 'bot_status_task' in globals():
            bot_status_task.cancel()
        if mode == 'static':
            await client.change_presence(activity=discord.Game(name=desc))
            await ctx.channel.send(embed=embed)
        elif mode == 'dynamic':
            desc = desc.split('|')
            await ctx.channel.send(embed=embed)
            bot_status_task = client.loop.create_task(status_task(desc))
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Not a valid mode!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

async def status_task(desc):
    while True:
        for i in desc:
            await client.change_presence(activity=discord.Game(name=i))
            await asyncio.sleep(4)

@cs.error
async def cs_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = user_cmd[1]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'${desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
