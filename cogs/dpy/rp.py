@client.command(description=str({"desc":"Renames project", "required_roles":None, "required_perms":None}))
async def rp(ctx, projectname, *, newprojectname):
    projectname = projectname.lower()
    newprojectname = newprojectname.lower()
    if get(ctx.guild.categories, name=f"{newprojectname} Dev") == None:
        if get(ctx.author.roles, name=f"{projectname} Founder"):
            founder = get(ctx.guild.roles, name=f"{projectname} Founder")
            dev = get(ctx.guild.roles, name=f"{projectname} Dev")
            category = get(ctx.guild.categories, name=f"{projectname} Dev")

            await founder.edit(name=f"{newprojectname} Founder")
            await dev.edit(name=f"{newprojectname} Dev")
            await category.edit(name=f"{newprojectname} Dev")
            
            await ctx.channel.send(f"Project **{projectname}** changed to **{newprojectname}**!")
        else:
            await ctx.channel.send('You must be the **__founder__** of the project to change the project name!')

    else:
        await ctx.channel.send("That project name already exists!")
