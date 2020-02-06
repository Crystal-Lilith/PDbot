@client.command()
async def rd(ctx, projectname, user):
    user = get(ctx.guild.members, name=user)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        if category == None:
            await ctx.channel.send("That **project** does not exist!")
        else:
            if user == None:
                await ctx.channel.send("That **user** does not exist!")
            else:
                await user.remove_roles(get(ctx.guild.roles, name=f"{projectname} Dev"))
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to add devs!')
