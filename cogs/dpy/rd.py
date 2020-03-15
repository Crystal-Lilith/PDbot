@client.command(description='Removes dev from a project||<username> <project-name>')
async def rd(ctx, user: discord.User, *, projectname):
    projectname = projectname.lower()
    user = ctx.guild.get_member(user.id)
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    if get(ctx.author.roles, name=f"{projectname} Founder"):
        if not user:
            embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                    description='That **user** does not exist!')
            embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            if not category:
                embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                        description='That **project** does not exist!')
                embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)
            else:
                if not get(user.roles, name=f"{projectname} Dev"):
                    embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                            description=f'User **{user}** is not part of the **{projectname}** Dev team!')
                    embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
                    await ctx.channel.send(embed=embed)
                else:
                    await user.remove_roles(get(ctx.guild.roles, name=f"{projectname} Dev"))
                    embed = discord.Embed(color=discord.Color.from_rgb(178, 34, 34),
                                            description=f'User **{user}** removed from **{projectname}** Dev!')
                    embed.set_footer(text=f'Dev removed by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
                    await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to add devs!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@rd.error
async def rd_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = user_cmd[1]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'${desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
