@client.command()
async def dp(ctx, projectname):
    await ctx.channel.purge(limit=1)
    channels = ['test']
    role = get(ctx.guild.roles, name=f"{projectname} Dev")
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    
    await role.delete()

    for i in channels:
        channel = get(ctx.guild.text_channels, name=i, category=category)
        await channel.delete()

    await get(ctx.guild.voice_channels, name='chat', category=category).delete()
    
    await category.delete()

    await ctx.channel.send(f"Category {projectname} deleted!")
