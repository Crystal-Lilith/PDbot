@client.command()
async def pc(ctx, hex, *, projectname):
    projectname = projectname.lower()
    color = discord.Color.from_rgb(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        await founder.edit(color=color)
        await dev.edit(color=color)
        await ctx.channel.send(f"The project color has been updated to **{hex}**!")
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to change the color!')
