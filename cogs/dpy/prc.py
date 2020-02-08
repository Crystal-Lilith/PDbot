@client.command()
async def(ctx, *, projectname):
    projectname = projectname.lower()
    color = discord.Color.from_rgb(randint(0,255), randint(0,255), randint(0,255))
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        await founder.edit(color=color)
        await dev.edit(color=color)
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to change the color!')
