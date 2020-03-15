@client.command(description='Renames project||<project-name> <new-project-name>')
async def rp(ctx, projectname, *, newprojectname):
    projectname = projectname.lower()
    newprojectname = newprojectname.lower()
    if get(ctx.guild.categories, name=f"{newprojectname} Dev"):
        if get(ctx.author.roles, name=f"{projectname} Founder"):
            founder = get(ctx.guild.roles, name=f"{projectname} Founder")
            dev = get(ctx.guild.roles, name=f"{projectname} Dev")
            category = get(ctx.guild.categories, name=f"{projectname} Dev")

            await founder.edit(name=f"{newprojectname} Founder")
            await dev.edit(name=f"{newprojectname} Dev")
            await category.edit(name=f"{newprojectname} Dev")
            
            embed = discord.Embed(color=discord.Color.from_rgb(0, 255, 0),
                                    description=f'Project **{projectname}** changed to **{newprojectname}**!')
            embed.set_footer(text=f'Project renamed by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to change the project name!')
            embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='That project name already exists!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@rp.error
async def rp_error(ctx, error):
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
