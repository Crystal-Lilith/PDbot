@client.command(description=str({"desc":"Deletes project", "required_roles":None, "required_perms":None}))
async def dp(ctx, *, projectname):
    projectname = projectname.lower()
    if get(ctx.author.roles, name=f"{projectname} Founder"):
        founder = get(ctx.guild.roles, name=f"{projectname} Founder")
        dev = get(ctx.guild.roles, name=f"{projectname} Dev")
        category = get(ctx.guild.categories, name=f"{projectname} Dev")

        while True:
            try:
                channel = get(ctx.guild.channels, category=category)
                await channel.delete()
            except:
                break
       
        await founder.delete()
        await dev.delete()
        
        await category.delete()

        await ctx.channel.send(f"Category **{projectname}** deleted!")
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to delete it!')
