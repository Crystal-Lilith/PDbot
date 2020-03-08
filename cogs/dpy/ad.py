@client.command(description='Adds a dev to your project||<username> <project-name>')
async def ad(ctx, user: discord.User, *, projectname):
    projectname = projectname.lower()
    user = ctx.guild.get_member(user.id)
    category = get(ctx.guild.categories, name=f'{projectname} Dev')

    if get(ctx.author.roles, name=f'{projectname} Founder'):
        if user != ctx.message.author:
            if not user:
                embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                        description='That **user** does not exist!')
                embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)
            else:
                if not category:
                    embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                            description='That **project** does not exist!')
                    embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
                    await ctx.channel.send(embed=embed)
                else:
                    if not get(user.roles, name=f'{projectname} Dev'):
                        await user.add_roles(get(ctx.guild.roles, name=f'{projectname} Dev'))
                        embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0),
                                                description=f'User **{user}** added to **{projectname} Dev**!')
                        embed.set_footer(text=f'Dev added by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
                        await ctx.channel.send(embed=embed)
                    else:
                        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                                description=f'User **{user}** is already a dev of **{projectname}**!')
                        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
                        await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                    description='You cannot add **yourself** as Dev!')
            embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to add devs!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@ad.error
async def ad_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = cmd.description.split('||')[0]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'{user_cmd[0]} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
