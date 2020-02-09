@client.command(description='Removes a dev from a project')
async def rd(ctx, user: discord.User, *, projectname):
    projectname = projectname.lower()
    user = ctx.guild.get_member(user.id)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        if user == None:
            await ctx.channel.send("That **user** does not exist!")
        else:
            if category == None:
                await ctx.channel.send("That **project** does not exist!")
            else:
                if get(user.roles, name=f"{projectname} Dev") == None:
                    await ctx.channel.send(f"User **{user}** is not part the **{projectname}** Dev team!")
                else:
                    await user.remove_roles(get(ctx.guild.roles, name=f"{projectname} Dev"))
                    await ctx.channel.send(f"User **{user}** removed from **{projectname}** Dev!")
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to add devs!')
