@client.command()
async def dp(ctx, projectname):
    await ctx.channel.purge(limit=1)
    channels = ['sources', 'to-do-list', 'suggestions', 'known-bugs', 'general', 'bot-commands']
    founder = get(ctx.guild.roles, name=f"{projectname} Founder")
    dev = get(ctx.guild.roles, name=f"{projectname} Dev")
    category = get(ctx.guild.categories, name=f"{projectname} Dev")
    
    if get(ctx.author.roles, name=f"{projectname} Founder"):
        await founder.delete()
        await dev.delete()

        for i in channels:
            channel = get(ctx.guild.text_channels, name=i, category=category)
            await channel.delete()

        await get(ctx.guild.voice_channels, name='chat', category=category).delete()
        
        await category.delete()

        await ctx.author.send(f"Category **{projectname}** deleted!", delete_after=60)
    else:
        await ctx.channel.send('You must be the __founder__ of the project to delete it!')
