@client.command()
async def rp(ctx, newprojectname, *, projectname):
    newprojectname = newprojectname.lower()
    projectname = projectname.lower()
    if get(ctx.guild.categories, name=f"{newprojectname} Dev") != None:
        if get(ctx.author.roles, name=f"{projectname} Founder"):
            founder = get(ctx.guild.roles, name=f"{projectname} Founder")
            dev = get(ctx.guild.roles, name=f"{projectname} Dev")
            category = get(ctx.guild.categories, name=f"{projectname} Dev")

            founder.edit(name=f"{newprojectname} Founder")
            dev.edit(f"{newprojectname} Dev")
            category.edit(f"{newprojectname} Dev")
            
            await ctx.channel.send(f"Project **{projectname}** changed to **{newprojectname}**!")
        else:
            await ctx.channel.send('You must be the **__founder__** of the project to change the project name!')

    else:
        await ctx.channel.send("That project name already exists!")
