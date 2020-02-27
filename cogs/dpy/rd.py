@client.command(description='Removes dev from a project')
async def rd(ctx, user: discord.User, *, projectname):
    projectname = projectname.lower()
    user = ctx.guild.get_member(user.id)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        if user:
            embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                    description='That **user** does not exist!')
            embed.set_footer(text=f'Attempted by: {ctx.message.author}')
            await ctx.channel.send(embed=embed)
        else:
            if category:
                embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                        description='That **project** does not exist!')
                embed.set_footer(text=f'Attempted by: {ctx.message.author}')
                await ctx.channel.send(embed=embed)
            else:
                if get(user.roles, name=f"{projectname} Dev"):
                    embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                            description=f'User **{user}** is not part the **{projectname}** Dev team!')
                    embed.set_footer(text=f'Attempted by: {ctx.message.author}')
                    await ctx.channel.send(embed=embed)
                else:
                    await user.remove_roles(get(ctx.guild.roles, name=f"{projectname} Dev"))
                    embed = discord.Embed(color=discord.Color.from_rgb(178, 34, 34),
                                            description=f'User **{user}** removed from **{projectname}** Dev!')
                    embed.set_footer(text=f'Dev removed by: {ctx.message.author}')
                    await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to add devs!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
