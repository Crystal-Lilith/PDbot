@client.command(description='Updates project color by Hex||<hex> <project-name>')
async def pc(ctx, _hex, *, projectname):
    projectname = projectname.lower()
    _hex = _hex.replace('#', '')
    color = discord.Color.from_rgb(*tuple(int(_hex[i:i+2], 16) for i in (0, 2, 4)))
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        await founder.edit(color=color)
        await dev.edit(color=color)
        embed = discord.Embed(color=discord.Color.from_rgb(178, 34, 34),
                                description=f'The project color has been updated to **{_hex}**!')
        embed.set_footer(text=f'Project color updated by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to change the color!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@pc.error
async def pc_error(ctx, error):
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
