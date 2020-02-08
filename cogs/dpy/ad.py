@client.command()
async def ad(ctx, user: discord.User, *, projectname):
    projectname = projectname.lower()
    user = get(ctx.guild.members, name=user)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        if user == None:
            await ctx.channel.send("That **user** does not exist!")
        else:
            if category == None:
                await ctx.channel.send("That **project** does not exist!")
            else:
                if get(user.roles, name=f"{projectname} Dev") == None:
                    await user.add_roles(get(ctx.guild.roles, name=f"{projectname} Dev"))
                    await ctx.channel.send(f"User **{user}** added to **{projectname} Dev**!")
                else:
                    await ctx.channel.send(f"User **{user}** is already a dev of **{projectname}**!")
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to add devs!')
