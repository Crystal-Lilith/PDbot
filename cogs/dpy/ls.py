@client.command(description='Shows you all files in the specified directory||<dir>')
@commands.has_any_role('PDBot Mod', 'PDBot Dev')
async def ls(ctx, *, directory='.'):
    try:
        x = ''
        split_directory = directory.split('/')
        for i in ['..']:
            if i in split_directory:
                embed = discord.Embed(title='Warning ❗', color=discord.Color.from_rgb(178, 34, 34),
                                description='You may not ls this directory!')
                embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)
                return
        for i in os.listdir(directory):
            if i.lower() not in ['.env', 'start.sh']:
                x = f"{x}{i}\n"
        embed = discord.Embed(title=f'List of files and folders in `{directory}`', color=discord.Color.from_rgb(0, 191, 255), 
                                description=f'```css\n{x}```')
        embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='Directory doesn\'t exist!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@ls.error
async def ls_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = user_cmd[1]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'${desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
