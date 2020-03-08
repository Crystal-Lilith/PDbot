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
            embed.set_footer(text=f'Project renamed by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to change the project name!')
            embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='That project name already exists!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)
