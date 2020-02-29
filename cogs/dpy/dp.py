@client.command(description='Deletes project||$dp <project-name>')
async def dp(ctx, *, projectname):
    projectname = projectname.lower()
    if get(ctx.author.roles, name=f"{projectname} Founder"):
        founder = get(ctx.guild.roles, name=f"{projectname} Founder")
        dev = get(ctx.guild.roles, name=f"{projectname} Dev")
        category = get(ctx.guild.categories, name=f"{projectname} Dev")

        while True:
            try:
                channel = get(ctx.guild.channels, category=category)
                await channel.delete()
                await asyncio.sleep(0.1)
            except:
                break
       
        await founder.delete()
        await dev.delete()
        
        await asyncio.sleep(0.1)
        await category.delete()

        embed = discord.Embed(color=discord.Color.from_rgb(178, 34, 34), description=f'Deleted {projectname}!')
        embed.set_footer(text=f'Project deleted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Error! ⚠️', color=discord.Color.from_rgb(255, 255, 51),
                                description='You must be the **__founder__** of the project to delete it!')
        embed.set_footer(text=f'Attempted by: {ctx.message.author}')
        await ctx.channel.send(embed=embed)
