@client.command()
async def dp(ctx, projectname):
    await ctx.channel.purge(limit=1)
    channels = ['test']
    category = get(ctx.guild.categories, name=f"{projectname} Dev")

    await ctx.role.delete(role = get(ctx.guild.roles, name=f"{projectname} Dev"))

    channels = get(ctx.guild.text_channels, name=i,category=category)
    await channels.delete()

    await get(ctx.guild.voice_channels, name='chat', category=category), category=category).delete()

    await ctx.category.delete()

    await ctx.channel.send(f"Category {projectname} deleted!")
