@client.command(description=str({"pc":{"desc":"Adds a dev to your project", "required_roles":None, "required_perms":None}}))
async def ad(ctx, user: discord.User, *, projectname):
    projectname = projectname.lower()
    user = ctx.guild.get_member(user.id)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        if user != ctx.message.author:
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
            await ctx.channel.send("You cannot add **yourself** as Dev!")
    else:
        await ctx.channel.send('You must be the **__founder__** of the project to add devs!')
