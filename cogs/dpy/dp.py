@client.command(description='Deletes project||<project-name>')
async def dp(ctx, *, projectname):
    projectname = projectname.lower()
    if get(ctx.author.roles, name=f"{projectname} Founder"):
        founder = get(ctx.guild.roles, name=f"{projectname} Founder")
        dev = get(ctx.guild.roles, name=f"{projectname} Dev")
        category = get(ctx.guild.categories, name=f"{projectname} Dev")

        await founder.delete()
        await dev.delete()

        while True:
            try:
                channel = get(ctx.guild.channels, category=category)
                await channel.delete()
                await asyncio.sleep(1)
            except:
                break
        
        await asyncio.sleep(1)
        await category.delete()

        embed = discord.Embed(color=discord.Color.from_rgb(178, 34, 34), description=f'Deleted **{projectname}**!')
        embed.set_footer(text=f'Project deleted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to delete it!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@dp.error
async def dp_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = await ctx.channel.fetch_message(ctx.message.id)
        user_cmd = message.content.split()[0].split('$')
        cmd = get(client.commands, name=user_cmd[1])
        desc = user_cmd[1]
        syntax = cmd.description.split('||')[1]
        embed = discord.Embed(title='Invalid Syntax! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description=f'${desc} ({syntax})')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
