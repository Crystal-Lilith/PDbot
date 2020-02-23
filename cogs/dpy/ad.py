@client.command(description='Adds a dev to your project')
async def ad(ctx, user: discord.User, *, projectname):
    projectname = projectname.lower()
    user = ctx.guild.get_member(user.id)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        if user != ctx.message.author:
            if user == []:
                embed = discord.Embed(title=f'Error!', color=discord.Color.from_rgb(255, 255, 51),
                                        description='That **user** does not exist!')
                embed.set_footer(text=f'Attempted By: {ctx.message.author}')
                await ctx.channel.send(embed=embed)
            else:
                if category == []:
                    embed = discord.Embed(title=f'Error!', color=discord.Color.from_rgb(255, 255, 51),
                                            description='That **project** does not exist!')
                    embed.set_footer(text=f'Attempted By: {ctx.message.author}')
                    await ctx.channel.send(embed=embed)
                else:
                    if get(user.roles, name=f"{projectname} Dev") == []:
                        await user.add_roles(get(ctx.guild.roles, name=f"{projectname} Dev"))
                        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0),
                                                description=f'User **{user}** added to **{projectname} Dev**!')
                        embed.set_footer(text=f'Created By: {ctx.message.author}')
                        await ctx.channel.send(embed=embed)
                    else:
                        embed = discord.Embed(title=f'Error!', color=discord.Color.from_rgb(255, 255, 51),
                                                description='User **{user}** is already a dev of **{projectname}**!')
                        embed.set_footer(text=f'Attempted By: {ctx.message.author}')
                        await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title=f'Error!', color=discord.Color.from_rgb(255, 255, 51),
                                    description='You cannot add **yourself** as Dev!')
            embed.set_footer(text=f'Attempted By: {ctx.message.author}')
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title=f'Error!', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to add devs!')
        embed.set_footer(text=f'Attempted By: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
