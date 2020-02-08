@client.command()
async def(ctx, red, green, blue, *, projectname):
    projectname = projectname.lower()
    color = discord.Color.from_rgb(red, gree, blue)
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        await founder.edit(color=color)
        await dev.edit(color=color)
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to change the color!')
