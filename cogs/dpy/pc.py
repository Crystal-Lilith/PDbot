@client.command(description=str({"desc":"Updates project color by Hex", "required_roles":None, "required_perms":None}))
async def pc(ctx, _hex, *, projectname):
    projectname = projectname.lower()
    _hex = _hex.replace('#', '')
    color = discord.Color.from_rgb(*tuple(int(_hex[i:i+2], 16) for i in (0, 2, 4)))
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        await founder.edit(color=color)
        await dev.edit(color=color)
        await ctx.channel.send(f"The project color has been updated to **{_hex}**!")
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to change the color!')
