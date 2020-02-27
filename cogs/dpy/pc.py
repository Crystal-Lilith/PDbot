@client.command(description='Updates project color by Hex')
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
        embed.set_footer(text=f'Project color updated by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to change the color!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
