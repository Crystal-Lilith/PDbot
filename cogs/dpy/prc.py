@client.command(description='Updates project with new random color')
async def prc(ctx, *, projectname):
    projectname = projectname.lower()
    color = discord.Color.from_rgb(randint(0,255), randint(0,255), randint(0,255))
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        await founder.edit(color=color)
        await dev.edit(color=color)
        embed = discord.Embed(color=discord.Color.from_rgb(178, 34, 34),
                                description=f'The project color has been updated to **{color}**!')
        embed.set_footer(text=f'Project color updated by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to change the color!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
